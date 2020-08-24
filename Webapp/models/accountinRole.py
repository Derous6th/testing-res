from models.dbContext import dbContext
class AccountInRole(dbContext):
    def add(self, arr):
        # Thieu
        #  sql = 'INSERT INTO AccountInRole(AccountId, RoleId) VALUES (?, ?)' [ chi add ko xoa dc ]
        sql = '{CALL AddAccountInRole(?, ?)}'
        return self.save(sql, arr)

    
    def getRolesByAccount(self, id):
        sql = 'SELECT RoleId FROM AccountInRole WHERE AccountId =? AND IsDeleted = 0'
        return self.fetchAll(sql, (id, ))