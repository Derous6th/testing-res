from models.dbContext import dbContext
class Account(dbContext):
    def fetch(self, sql, arr ):
        v = self.fetchOne(sql, arr)
        if v:
            return {'id': v[0], 'usr': v[1], 'eml': v[2]}


    def getAccount(self, arr):
        sql = 'SELECT AccountId, Username, Email FROM Account WHERE Username = ? AND Password = ?'
        return self.fetch(sql, arr)


    def getAccounts(self):
        return self.fetchAll('SELECT * FROM Account')


    def getAccountsById(self, id):
        sql = 'SELECT AccountId, Username, Email FROM Account WHERE AccountId = ?'
        return self.fetch(sql, (id, ))


    def getAccountBySession(self, id):
        sql = 'SELECT Account.AccountId, Username, Email FROM Account JOIN Session On Account.AccountId = Session.AccountId WHERE SessionId = ? AND IsDeleted = 0'
        return self.fetch(sql, (id, ))
        

    def add(self, arr):
        sql = '{CALL AddAccount (?, ?, ?, ?)}'
        return self.save(sql, arr)


    def add2(self, arr):
        sql = '{CALL AddAccount2 (?, ?, ?, ?)}'
        return self.save(sql, arr)
