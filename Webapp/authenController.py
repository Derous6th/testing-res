from flask import Flask, render_template, redirect, make_response, request
from models.session import Session
from models.account import Account
from util import randomStr
from hashlib import md5

app = Flask(__name__)

@app.route('/authen')
def index():
    if request.cookies.get('session'):
        acc = Account()
        v = acc.getAccountBySession(request.cookies.get('session'))
        return render_template('authen/index.html', v = v)
    return redirect('authen/signin')
@app.route('/authen/signin')
def signin():
    return render_template('authen/signin.html')
@app.route('/authen/signin', methods=['post'])
def doSignin():
    usr = request.form.get('usr')
    pwd = request.form.get('pwd') + '!@$*&#' + usr 
    pwd = md5(pwd.encode()) 
    rem = request.form.get('rem')
    acc = Account()
    v = acc.getAccount( (usr,pwd.digest()))
    if v:
        res = make_response(redirect('/authen'))
        #set cookies
        token = randomStr(32)
        ses = Session()
        ret = ses.add((token, v['id']))
        if rem == '1':
            res.set_cookie('session', token, max_age= 69 * 24 * 3600)
        else:
            res.set_cookie('session', token)
        return res
    return render_template('authen/signin.html', err = 'Sign in Failed')


@app.route('/authen/signout', methods=['GET','POST']) #dung <a> thi GET
def signout():
    if request.cookies.get('session'):
        ses = Session()
        ret = ses.delete(request.cookies.get('session'))

        res = make_response(redirect('/authen/signin'))
        res.set_cookie('session', '', max_age= -1)
        return res
    return redirect('authen/signin')


app.run(debug=True)