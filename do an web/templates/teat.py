from flask import Flask
from flask import render_template
from flask import request
from flask_dropzone import Dropzone
import os
app = Flask(_name_)
dropzone = Dropzone(app)
@app.route ("/")
@app.route ("/index")
def index():
    sample_var = list(range (10))
    print(sample_var)
    return render_template('index.html', the_title ='Tiger 1', sample_var = sample_var )
@app.route ("/myth")
def myth():
    return render_template('index.html', the_title ='This is hello thai')
@app.route('/upload', methods = ['GET','POST'])
def upload():
    if request.method == 'PORT':
           f = request.files.get('file')
           f.save(os.path.join(os.getCwd(),'static','imges',f.filename))
           return 'upload template'
    return render_template('upload.html', the_title= 'Upload From')
@app.route ("/symbol")
def symbol():
    return render_template('index.html', the_title ='This is symbol ')
if _name_ =="_main_":
    app.run(debug=True)