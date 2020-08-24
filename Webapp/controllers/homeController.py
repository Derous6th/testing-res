from flask import Blueprint, render_template, request, redirect, Flask
from models.category import Category
from models.brand import Brand
from models.product import Product
home = Blueprint('home', __name__)
@home.route('/')
def index():
    cat = Category()
    brd = Brand()
    arr = Product()
    a = arr.getProducts()
    b = brd.getBrands()
    c = cat.getCategories()
    return render_template('home/index.html', arr = a, brr = b, crr = c )


@home.route('/home/cat/<int:id>')
def cat(id):
    cat = Category()
    brd = Brand()
    arr = Product()
    a = arr.getProductsByCategory(id)
    b = brd.getBrands()
    c = cat.getCategories()
    return render_template('home/index.html', arr = a, brr = b, crr = c )


@home.route('/home/brand/<int:id>')
def brd(id):
    cat = Category()
    brd = Brand()
    arr = Product()
    a = arr.getProductByBrand(id)
    b = brd.getBrands()
    c = cat.getCategories()
    return render_template('home/index.html', arr = a, brr = b, crr = c )


@home.route('/home/detail/<int:id>')
def detail(id):
    cat = Category()
    brd = Brand()
    arr = Product()
    a = arr.getProductById(id)
    b = brd.getBrands()
    c = cat.getCategories()
    d = arr.getProductsRelation(id)
    return render_template('home/detail.html', prod = a, brr = b, crr = c , arr = d )