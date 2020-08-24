from pyodbc import connect

class DataRaw:
    def __init__(self):
        self.db = connect('Driver={SQL Server};Server=PM408-15\\MSSQLSERVER2014;DATABASE=Store;Trusted_connection=True')
    def add(self, a):
        cur = self.db.cursor()
        sql = '''INSERT INTO DataRaw(RowID, OrderID, OrderDate, ShipMode, CustomerId, CustomerName) VALUES (?, ?, ?, ?, ?, ?)'''
        cur.executemany(sql, a)
        self.db.commit()
        cur.close()
    def count(self):
        cur = self.db.cursor()
        sql = 'SELECT COUNT(*) FROM DataRaw'
        cur.execute(sql)
        c = cur.fetchone()
        cur.close()
        return c[0]
    def getDataRaws(self, pageIndex, pageSize = 10):
        cur = self.db.cursor()
        cur.execute('SELECT * FROM DataRaw ORDER BY RowID OFFSET ? ROWS FETCH NEXT ? ROWS ONLY',(( pageIndex - 1 ) * pageSize), pageSize)
        a = cur.fetchall()
        cur.close()
        return a

    def __del__(self):
        self.db.close()