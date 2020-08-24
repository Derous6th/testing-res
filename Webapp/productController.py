from flask import Flask, redirect, render_template, request
from models.product import Product
from models.category import Category
app = Flask(__name__)

@app.route('/product')
def index():
    pro = Product()
    return render_template('product/index.html', arr= pro.getProducts())

@app.route('/product/add')
def add():
    cat = Category()
    return render_template('product/add.html', arr = cat.getCategories())

@app.route('/product/add', methods=['POST'])
def doAdd():
    f = request.files.get('f')
    f.save('static/photos/' + f.filename)
    a = (request.form.get('Cat'),request.form.get('name'),request.form.get('pri'), f.filename ,request.form.get('des'),request.form.get('qty'))
    pro = Product()
    ret = pro.add(a)
    print('-----',ret)
    if ret > 0:
        return redirect('/product')
    return 'Failed'

@app.route('/product/edit/<id>')
def edit(id):
    cat = Category()
    pro = Product()
    a = cat.getCategories()
    b = pro.getProductById(id)
    return render_template('product/edit.html', arr =a , u = b)

@app.route('/product/delete/<id>')
def delete(id):
    pro = Product()
    return str(pro.delete(id)) #co ham nay de xoa tren database

@app.route('/product/edit2/<id>')
def edit2(id):
    cat = Category()
    pro = Product()
    a = cat.getCategories()
    b = pro.getProductById(id)
    print(b)
    return render_template('product/edit2.html', arr =a , u = b)

@app.route('/product/edit/<id>', methods=['POST'])
def doEdit(id):
    img = request.form.get('img')  #neu co san hinh va ko thay doi, gan IMG = file cu co san
    f = request.files.get('f')
    if f: #neu upload anh moi
        f.save('/static/photos/' + f.filename)
        img = f.filename
    a = (request.form.get('cat'),request.form.get('name'),request.form.get('pri'), img ,request.form.get('des'),request.form.get('qty'), id)
    cat = Product()
    ret = cat.edit(a)
    if ret > 0:
        return redirect('/product')
    return 'Failed'



app.run(debug = True )