from models.category import Category
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/category')
def index():
    #khoi tao lop:
    cat = Category()
    #goi ham

    a = cat.getCategories()

    return render_template('category/index.html', arr = a)

@app.route('/category/delete/<id>')
def delete(id):

    cat = Category()

    ret = cat.delete(id)
    if ret > 0:
        return redirect('/category')
    return 'Failed'

@app.route('/category/edit/<id>')
def edit(id):
    cat = Category()
    v = cat.getCategoryById(id)
    print(v)
    return render_template('/category/edit.html' , i = v )

@app.route('/category/edit/', methods=['POST'])
def doEdit(id):
    cat = Category()
    a = (request.form.get('name'), id)
    ret = cat.Edit(a)
    if ret > 0:
        return redirect('/category')
    return 'Failed'

@app.route('/category/delall', methods=['post'])
def delall():
    #a = req
    a = request.form.getlist('a')
    #simple###########
    #cat = Category()
    #ret = 0
    #print('a =',len(a))
    #for i in a:
        #ret += cat.delete(i)
    #if ret >= len(a):
        #return redirect('/category')
    #return 'Failed'
    ###########################
    
    #arrayDelete
    arr = []
    cat = Category()
    ret = 0
    for i in a:
        arr.append((i, ))
    ret = cat.deleteAll(arr)
    return redirect('/category')

app.run(debug = True)
