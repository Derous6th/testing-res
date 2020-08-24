from models.dbContext import dbContext
class Role(dbContext):
    def getRoles(self):
        sql = 'SELECT * FROM Role'
        return self.fetchAll(sql)


    def getRolesByAccount(self, id):
        sql = '''SELECT Role.*, IIF(AccountId IS NULL, 0 , 1)
	        FROM AccountInRole RIGHT JOIN Role ON AccountInRole.RoleId = Role.RoleId
	        AND AccountId = ? AND IsDeleted = 0 '''
        return self.fetchAll(sql, (id, ))
    
    def add(self, arr):
        sql = 'INSERT INTO Role (RoleId, RoleName) VALUES (?, ?)'
        return self.save(sql, arr)