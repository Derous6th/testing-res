from flask import Flask, render_template, request, redirect, jsonify
from models.account import Account
from models.accountinRole import AccountInRole
from models.role import Role
app = Flask(__name__)

@app.route('/account')
def index():
    acc = Account()
    ro = Role()
    return render_template('account/index.html', arr = acc.getAccounts(), brr = ro.getRoles())


@app.route('/account/json/<id>')
def json(id):
    air = AccountInRole()
    a = air.getRolesByAccount(id)
    dic = {}
    for v in a:
        dic[v[0]] = 1
    return jsonify(dic)

@app.route('/account/role/<id>')
def role(id):
    acc = Account()
    x = acc.getAccountsById(id)
    #  Thieu
    ro = Role()
    air = AccountInRole()
    #  Transfer
    #  List
    a = air.getRolesByAccount(id)
    li = []
    for v in a:
        li.append(v[0])
    #  Diction
    return render_template('account/role.html', a = x, arr = ro.getRoles(), brr = li)


#  Role 2 dung SQL, JOIN 
@app.route('/account/role2/<id>')
def role2(id):
    acc = Account()
    x = acc.getAccountsById(id)
    #  Thieu
    ro = Role()
    #  Dictionary
    b = ro.getRolesByAccount(id)
    #  print('--------', b)
    return render_template('account/role2.html', a = x, arr = b)

@app.route('/account/addrole', methods=['POST'])
def addRole():
    roleID = request.form.get('roleID')
    accID = request.form.get('accID')
    air = AccountInRole()
    return str(air.add((accID,roleID)))


app.run(debug=True)