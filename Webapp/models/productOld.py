from pyodbc import connect
class Product:
    def __init__(self):
        self.db = connect('Driver={SQL Server};Server=PM408-14\MSSQLSERVER2014;Database=Store;Trusted_Connect=True')

    def add(self,arr):
        sql = ''' INSERT INTO Product ( CategoryId, ProductName, Price, ImageUrl, Description, Quantity) VALUES(?, ?, ?, ?, ?, ?)'''
        cur = self.db.cursor()
        cur.execute(sql, arr)
        ret = cur.rowcount
        self.db.commit()
        cur.close
        return ret

    def edit(self,arr):
        sql = '''UPDATE Product SET CategoryId = ?, ProductName = ?, Price = ?, ImageUrl = ?, Description = ?, Quantity = ? WHERE ProductId = ?'''
        cur = self.db.cursor()
        cur.execute(sql, arr)
        ret = cur.rowcount
        self.db.commit()
        cur.close()
        return ret
    
    def delete(self,id):
        cur = self.db.cursor()
        cur.execute('DELETE Product WHERE ProductId = ?', (id, ))
        ret = cur.rowcount
        self.db.commit()
        cur.close()
        return ret

    def getProducts(self):
        cur = self.db.cursor()
        cur.execute('SELECT * FROM Product')
        a = cur.fetchall()
        cur.close()
        return a

    def getProductById(self,id):
        cur = self.db.cursor()
        cur.execute('SELECT * FROM Product WHERE ProductId =?', (id, ))
        u = cur.fetchone()
        cur.close()
        return u

    def __del__(self):
        self.db.close()
            