import pyodbc
cnxn_str = ("Driver={SQL Server};"
            "Server=DESKTOP-9DHBJDE;"
            "Database=Learning;"
            "UID=sa;PWD=Umasslowel24!")
cnxn = pyodbc.connect(cnxn_str)
cursor  =cnxn.cursor()

cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()
    