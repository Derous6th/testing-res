from flask import Flask, render_template, request, redirect , session
from models.account import Account
from random import choice
from hashlib import md5
app = Flask(__name__)

app.secret_key = 'admziasjdamqwkakx'
@app.route('/auth/signup')
def signup():
    return render_template('auth/signup.html')
@app.route('/auth/register')
def register():
    return render_template('auth/signup.html')
def randomStr(len):
    a = []
    p = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    for i in range(len):
        a.append(choice(p))
    return ''.join(a)

#Cach hash pw 1 SQL[ dung profiler thay pw ]
@app.route('/auth/register', methods=['post'])
def doRegister():
    id = randomStr(16)
    usr = request.form.get('usr')
    pwd = request.form.get('pwd')
    eml = request.form.get('eml')
    pwd = md5(pwd.encode()) + '!@$*&#' + usr #tranh crack pw
    acc = Account()
    ret = acc.add2( (id, usr, pwd.digest(), eml))
    if ret > 0:
        return redirect('/auth/signin')
    return render_template('auth/register.html', err = 'Username exists')
@app.route('/auth/signup', methods=['post'])

#Cach hash pw 2 Python[ dung profiler thay hashed pw ]
def doSignup():
    id = randomStr(16)
    usr = request.form.get('usr')
    pwd = request.form.get('pwd') + '!@$*&#' + usr #tranh crack pw
    eml = request.form.get('eml')
    pwd = md5(pwd.encode())
    acc = Account()
    ret = acc.add( (id, usr, pwd.digest(), eml))
    if ret > 0:
        return redirect('/auth/signin')
    return render_template('auth/signup.html', err = 'Username exists')
@app.route('/auth')
def index():
    if 'userinfo' in session:
        return render_template('auth/index.html')
    return redirect('/auth/login')
@app.route('/auth/signin')
def signin():
    return render_template('auth/signin.html')

@app.route('/auth/signin', methods = ['post'])
def doSignin():
    usr = request.form.get('usr')
    pwd = request.form.get('pwd') + '!@$*&#' + usr #phai giong voi signup
    pwd = md5(pwd.encode()) 
    acc = Account()
    v = acc.getAccount( (usr,pwd.digest()) )
    if v:
        session['userinfo'] = v #Session variables remember data from request to request, and specifically for each user. Account info is one type of data stored in a session object.
    else:
        return render_template('auth/signin.html', err = 'Wrong Username or Password')
    return redirect('/auth')

@app.route('/auth/signout')
def signout():
    if 'userinfo' in session:
        session.pop('userinfo')
    return redirect('/auth/signin')

app.run(debug=True)