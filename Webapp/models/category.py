from models.dbContext import dbContext
class Category(dbContext):
    #  Home Project 23-08-20
    def getCategories(self):
        sql = 'SELECT * FROM production.Category'
        return self.fetchAll(sql)
    
    
    