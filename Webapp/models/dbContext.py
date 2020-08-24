from pyodbc import connect
class dbContext:
    def __init__(self):
        db = 'Driver={SQL Server};Database=BikeStore;Server=PM408-14\MSSQLSERVER2014;Trusted_Connection=Yes'
        self.db = connect(db)
    
    def __del__(self):
        self.db.close()

    def save(self, sql, arr):
        cur = self.db.cursor()
        cur.execute(sql, arr)
        ret = cur.rowcount
        self.db.commit()
        cur.close()
        return ret

    def fetchOne(self, sql, arr):
        cur = self.db.cursor()
        cur.execute(sql, arr)
        v = cur.fetchone()
        cur.close()
        return v

    def fetchAll(self, sql, arr = None):
        cur = self.db.cursor()
        if arr:
            cur.execute(sql, arr)
        else:
            cur.execute(sql)
        a = cur.fetchall()
        cur.close()
        return a