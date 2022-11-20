import pyodbc
#OnPremise SSMS Server
onPremiseConnection = pyodbc.connect(
          "DRIVER={ODBC driver 17 for SQL Server};"
          "Server=xxx;"
          "Database=xxx;"
          "Trusted Connection=yes;"
)
onPremisecursor =onPremiseConnection.cursor()
onPremisecursor.execute("#SQL SCRIPT#")

result = onPremisecursor.fetchall()

for onPremiseRow in result:
    print(onPremiseRow)
    print("\n")

onPremisecursor.close()
onPremiseConnection.close()

#Azure Server

azureConnection = pyodbc.connect(
               "DRIVER={ODBC driver 17 for SQL Server};"
               "Server=xxx;"
               "Database=xxx;"
               "Uid=xxx;"
               "Pwd=xxx;"
               "Trusted Connection=no;"
               "Connection Timeout=30;"
)

azureCursor = azureConnection.cursor()
azureCursor.execute("#SQL SCRIPT#")
azureRow = azureCursor.fetchone()

while azureCursor:
    print(str(azureRow[0]) + " " + str(azureRow[1]))
    azureRow = azureCursor.fetchone()