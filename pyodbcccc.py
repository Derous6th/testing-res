from pyodbc import connect
db = connect('Driver={SQL Server};Server=PM408-15\\MSSQLSERVER2014;DATABASE=Store;Trusted_connection=True')
#print(db)
cur = db.cursor()
cur.execute('SELECT * FROM Member')
arr = cur.fetchall()
print(arr)
cur.close()
db.close()
