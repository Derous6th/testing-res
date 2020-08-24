from models.dbContext import dbContext
class Product(dbContext):
    def getProducts(self):
        sql = 'SELECT * FROM production.Product ORDER BY ProductId OFFSET 0 ROWS FETCH NEXT 18 ROWS ONLY'
        return self.fetchAll(sql)


    def getProductsByCategory(self, id):
        sql = 'SELECT * FROM production.Product WHERE CategoryId = ?'
        return self.fetchAll(sql, (id, ))


    def getProductByBrand(self, id):
        sql = 'SELECT * FROM production.Product WHERE BrandId = ?'
        return self.fetchAll(sql, (id, ))

    
    def getProductById(self, id):
        sql = 'SELECT * FROM production.Product WHERE ProductID = ?'
        return self.fetchOne(sql, (id, ))


    def getProductsRelation(self, id):
        sql = '''SELECT p.* FROM production.Product as p join 
            (SELECT * FROM production.Product WHERE ProductId = ?) as tbl
            ON p.BrandId = tbl.BrandId AND p.CategoryId = tbl.CategoryId'''
        return self.fetchAll(sql, (id, ))