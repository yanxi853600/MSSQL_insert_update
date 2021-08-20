# 讓各種db能夠通用的格式
#1. 搜尋key value，若無資料則insert data
#2. 若有資料則update data 
## Insert_update(TableName, {"Status":-1,...}, pk)
#==============================================
#import pymssql
import urllib
import pyodbc
pyodbc.pooling = False
import sqlalchemy
import pandas as pd
import numpy as np

class msSQL:
    global fill_null
    global json_colval
    
    def connect(self,DRIVER,SERVER,DATABASE):
        terms = urllib.parse.quote_plus(
            'DRIVER='+DRIVER+';'
            'SERVER='+SERVER+';'
            'DATABASE='+DATABASE+';'
            'Trusted_Connection=yes;')
        url = f'mssql+pyodbc:///?odbc_connect={terms}'
        engine = sqlalchemy.create_engine(url, fast_executemany=True)

        return engine

    def fill_null(vals: list) -> list:
        def bad(val):
            if isinstance(val, type(pd.NA)):
                return True
            return val in ['NULL', np.nan, 'nan', ' ', '', '-', '?']
        return tuple(i if not bad(i) else None for i in vals)

    def json_colval(self, json_txt):    
        ##Get ColumnName
        df = pd.json_normalize(json_txt)
        ColumnName_list = df.columns.values.tolist()
        ColumnName = f'({(", ".join(ColumnName_list))})'

        ##Get Value
        GetValue_list = df.iloc[0].values.tolist()
        GetValue = "('"+"','".join(["".join(str(GetValue_list)) for GetValue_list in GetValue_list])+"')"

        return ColumnName_list, ColumnName, GetValue

    def insert(self, json_txt):
        #columns name
        global cols_list_query
        global sr_cols_list_query

        ColumnName_list, ColumnName, GetValue = json_colval(json_txt, json_txt)
        cols_list_query = f'({(", ".join(ColumnName_list))})'
        #insert data
        sr_cols_list = [f'Source.{i}' for i in ColumnName_list]
        sr_cols_list_query = f'({(", ".join(sr_cols_list))})'

        return GetValue

    def update(self, json_txt):
        #update data
        ColumnName_list, ColumnName, GetValue = json_colval(json_txt, json_txt)
        up_cols_list = [f'{i}=Source.{i}' for i in ColumnName_list]
        up_cols_list_query = f'{", ".join(up_cols_list)}'
        return up_cols_list_query
 
    
## 1. Connect_to_db 2. Table_pk_Insert_Update
class Execute:
    def sql_connect(Driver, SERVER, DATABASE):
        global sql_conn
        conn = msSQL()
        sql_conn = conn.connect(Driver,SERVER,DATABASE).begin()
        print("Sucessfully connected to database!") 

    def insert_update(TableName, pk, json_txt): 
        conn = msSQL()
        cmd = f'''MERGE INTO {TableName} as Target USING (SELECT * FROM (VALUES {conn.insert(json_txt)}) AS s {cols_list_query} ) AS Source ON Target.{pk}=Source.{pk} WHEN NOT MATCHED THEN INSERT {cols_list_query} VALUES {sr_cols_list_query}  WHEN MATCHED THEN UPDATE SET {conn.update(json_txt)};'''
        with sql_conn as connn:
            connn.execute(cmd)  
            print('Successfully to Insert or Update!')


if __name__ == '__main__': 
    # sql_connect(Driver, SERVER, DATABASE)
    Execute.sql_connect('ODBC Driver 17 for SQL Server','.\SQLEXPRESS','TWM9')
    # insert_update(TableName, pk, json_txt)
    Execute.insert_update('[TW].[dbo].[AI_Work_Final]', 'DateTime', {"Camera_ID":"6de2b29e-a7d5","DateTime":"2021-06-18 16:22:00","Status":5}) 