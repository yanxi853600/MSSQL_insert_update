SGA: Operation in python with SQL Server
===
Insert or Update database in a flexable way

* python = 3.6.9



# SGA: SQL Server_python
--------------------------------

![alt text](https://dev.azure.com/SE-Develop/6c9779dc-21a0-4509-ae29-f440d2e5d1db/_apis/git/repositories/e851384d-c6ed-40eb-973d-368eb5154dac/items?path=%2Fmssql_process.png&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0)

# Client to call the function
--------------------------------

### SQL Connect function
```
# sql_connect(Driver, SERVER, DATABASE)
Execute.sql_connect('ODBC Driver 17 for SQL Server','.\SQLEXPRESS','TWM9')
```
![alt text](https://dev.azure.com/SE-Develop/6c9779dc-21a0-4509-ae29-f440d2e5d1db/_apis/git/repositories/e851384d-c6ed-40eb-973d-368eb5154dac/items?path=%2Fmssql_process.png&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0)


### Insert or Update function
```
# insert_update(TableName, pk, json_txt)
Execute.insert_update('[TWM9].[dbo].[m9_2col]', 'DateTime', {"Camera_ID":"6de2b29e-a7d5-532b-bebd-762968332b6a","DateTime":"2021-06-21 10:37:00"}) # ,"Status":5
```
![alt text](https://dev.azure.com/SE-Develop/6c9779dc-21a0-4509-ae29-f440d2e5d1db/_apis/git/repositories/e851384d-c6ed-40eb-973d-368eb5154dac/items?path=%2Fmssql_process.png&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0)
