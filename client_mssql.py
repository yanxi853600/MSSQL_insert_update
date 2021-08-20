from SGA_msSQL_finish import Execute

# sql_connect(Driver, SERVER, DATABASE)
Execute.sql_connect('ODBC Driver 17 for SQL Server','.\SQLEXPRESS','TW')
# insert_update(TableName, pk, json_txt)
Execute.insert_update('[TW].[dbo].[2col]', 'DateTime', {"Camera_ID":"6de2b29e-a7d5","DateTime":"2021-06-21 16:22:00"}) # ,"Status":5