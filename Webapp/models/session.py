from models.dbContext import dbContext
class Session(dbContext):
    
    def add(self,arr):
        sql = 'INSERT INTO Session(SessionId, AccountId) VALUES (?, ?)'
        return self.save(sql, arr)
    
    def delete(self,id ):
        sql = 'UPDATE Session SET IsDeleted = 1 WHERE SessionId = ?'
        return self.save(sql, (id, ))
    