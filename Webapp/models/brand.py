from models.dbContext import dbContext
class Brand(dbContext):
    def getBrands(self):
        sql = 'SELECT * FROM production.Brand'
        return self.fetchAll(sql)


    