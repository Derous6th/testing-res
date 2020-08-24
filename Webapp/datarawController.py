from flask import Flask, render_template, redirect, request
from models.dataraw import DataRaw
from pandas import read_excel
app = Flask(__name__)

@app.route('/dataraw')
@app.route('/dataraw/<int:p>')
def index(p = 1):
    dr = DataRaw()
    c = dr.count()
    pageSize = 1000
    n = c // pageSize
    if c % pageSize > 0:
        n += 1
    return render_template('dataraw/index.html', arr = dr.getDataRaws(p, pageSize), n = n, c = c)
@app.route('/dataraw/import')
def importdata():
    return render_template('dataraw/import.html')
@app.route('/dataraw/import', methods=['POST'])
def doImportData():
    f = request.files.get('f')
    url = 'static/data/' + f.filename
    f.save(url)
    df = read_excel(f)
    a = []
    for i in df.index:
    #print(df['Order ID'][i], df['Order Date'][i], df['Ship Mode'][i], df['CustomerID'][i], df['Customer Name'][i])
        a.append((int(df[('Row ID')][i]),
        df['Order ID'][i],
        df['Order Date'][i],
        df['Ship Mode'][i],
        df['Customer ID'][i], 
        df['Customer Name'][i]))
    db = DataRaw()
    db.add(a)
    return redirect('/dataraw')

app.run(debug=True)