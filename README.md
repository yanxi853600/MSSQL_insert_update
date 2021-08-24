Operation in python with SQL Server
===
Insert or Update database in a flexable way

* python = 3.6.9



# SQL Server_python
--------------------------------

![alt text](https://github.com/yanxi853600/MSSQL_insert_update/blob/master/mssql_process.png)

# Client to call the function
--------------------------------

### SQL Connect function
```
# sql_connect(Driver, SERVER, DATABASE)
Execute.sql_connect('ODBC Driver 17 for SQL Server','.\SQLEXPRESS','TW')
```
![alt text](https://github.com/yanxi853600/MSSQL_insert_update/blob/master/2_col.JPG)


### Insert or Update function
```
# insert_update(TableName, pk, json_txt)
Execute.insert_update('[TW].[dbo].[2col]', 'DateTime', {"Camera_ID":"6de2b29e","DateTime":"2021-06-21 10:37:00"}) # ,"Status":5
```
![alt text](https://github.com/yanxi853600/MSSQL_insert_update/blob/master/3_col.JPG)
