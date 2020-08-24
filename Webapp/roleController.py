from flask import Flask, render_template, request, redirect, jsonify
from models.role import Role
from random import randint
app = Flask(__name__)
@app.route('/role')
def index():
    ro = Role()
    return render_template('role/index.html', arr = ro.getRoles())


@app.route('/role/add', methods=['POST'])
def add():
    ro = Role()
    name = request.form.get('name')
    id = randint(10000,99999)
    ro.add((id, name))
    return redirect('/role')


@app.route('/role/create', methods=['POST'])
def create():
    ro = Role()
    name = request.form.get('name')
    id = randint(10000,99999)
    if ro.add((id, name)) > 0:
        return jsonify({'id': id, 'name': name})
    return 'Failed'

    
app.run(debug=True)
