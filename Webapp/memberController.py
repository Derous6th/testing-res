from flask import Flask, render_template, redirect, request
from pyodbc import connect
from models.randomfunct import randomStr
app = Flask(__name__)

@app.route('/member')
def index():
    db = connect('Driver={SQL Server};Database=Store;Server=PM408-18\MSSQLSERVER2014;Trusted_connection=True')
    cur = db.cursor()
    cur.execute('SELECT * FROM Member')
    arr = cur.fetchall()
    cur.close()
    db.close()
    return render_template('member/index.html', arr = arr)

@app.route('/member/add')
def add():
    return render_template('member/add.html')

@app.route('/member/add', methods = ['POST'])
def doAdd():
    id = randomStr(16)
    usr = request.form.get('username')
    pwd= request.form.get('password')
    fn = request.form.get('fullname')
    gen = request.form.get('gender')
    adr = request.form.get('address')
    dob = request.form.get('dateofbirth')

    db = connect('Driver={SQL Server};Database=Store;Server=PM408-15\MSSQLSERVER2014;Trusted_connection=True')
    cur = db.cursor()
    
    sql = '''INSERT INTO Member
        (MemberId, Username, Password, Fullname, Address, Gender, DateOfBirth)
        VALUES (?,?,?,?,?,?,?)'''
    
    cur.execute(sql, (id,usr,pwd,fn,adr,gen,dob))

    ret = cur.rowcount

    db.commit()
    cur.close()
    db.close()

    if ret > 0:
        return redirect('/member')
    return 'Failed'

@app.route('/member/delete/<id>')
def doDelete(id):
    db = connect('Driver={SQL Server};Database=Store;Server=PM408-15\MSSQLSERVER2014;Trusted_connection=True')
    cur = db.cursor()
    cur.execute('DELETE Member WHERE MemberId = ?', (id, ))
    ret = cur.rowcount
    db.commit()
    cur.close()
    db.close()
    if ret > 0:
        return redirect('/member')
    return 'Failed'
    

app.run(debug=True)