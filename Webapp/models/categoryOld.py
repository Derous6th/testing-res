from models.dbContext import dbContext
class Category(dbContext):
    #def getCategories(self):
        #cur = self.db.cursor()
        #thuc thi truy van
        #cur.execute('SELECT * FROM Category')
        #doc du lieu ve
        #arr = cur.fetchall()
        #dong cursor
        #cur.close()
        #return arr


    def getCategoryById(self, id):
        cur = self.db.cursor()
        cur.execute('SELECT * FROM Category WHERE CategoryId =?', (id, ))
        v = cur.fetchone()
        cur.close()
        return v
    

    def Edit(self, arr):
        cur = self.db.cursor()
        cur.execute('UPDATE Category SET CategoryName = ? WHERE CategoryId =?', arr)
        ret = cur.rowcount
        self.db.comit()
        cur.close()
        return ret
    

    def delete(self,id):
        cur = self.db.cursor()
        cur.execute('DELETE Category WHERE CategoryId = ?', (id, ))
        ret = cur.rowcount
        self.db.commit()
        cur.close()
        return ret
    

    def deleteAll(self,arr):
        cur = self.db.cursor()
        cur.executemany('DELETE Category WHERE CategoryId =?', arr)
        ret = cur.rowcount
        self.db.commit()
        cur.close()
        return ret
    

    