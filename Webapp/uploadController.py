from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/upload')
def index():
    return render_template('upload/index.html')

@app.route('/upload', methods=['POST'])
def doIndex():
    f = request.files['f'];
    f.save('static/upload/' + f.filename)
    return render_template('upload/index.html', img = f.filename)

@app.route('/upload/multiple')
def multiple():
    return render_template('upload/multiple.html')
@app.route('/upload/multiple', methods =['POST'])
def doMultiple():
    a = request.files.getlist('f');
    b= []
    for f in a :
        f.save('static/photo' + f.filename)
        b.append(f.filename)
    return render_template('upload/multiple.html', brr= b)


app.run(debug= True)
