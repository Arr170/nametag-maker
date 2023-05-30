from flask import Flask, request, make_response, url_for, redirect, send_file, render_template
from flask_cors import CORS
import os
import big_size
import small_size_new
import big_size_names

app = Flask(__name__,template_folder='frontend/build', static_folder='frontend/build/static')
CORS(app)


UPLOAD_FOLDER = './uploaded'

@app.route("/test", methods = ['POST', 'GET'])
def hello():
    if request.method == 'GET':
        return {
            "one":[ "one", "two"],
            "two": "two"
        }

@app.route("/", methods = ['POST', 'GET'])
def home():
   return render_template('index.html')

@app.route("/Small", methods = ['POST', 'GET'])
def small():
   return render_template('index.html')

@app.route("/Big", methods = ['POST', 'GET'])
def big():
   return render_template('index.html')
#server gets csv file, template name and competition name from frontend
@app.route("/bigsizeStats", methods = ['POST'])
def do_big():      
    uploaded_files = request.files['file']
    uploaded_files.save(os.path.join(UPLOAD_FOLDER, uploaded_files.filename))
    compN = request.form['compN']
    template = request.form['template']
    print('#######', template)
    src = os.path.join(UPLOAD_FOLDER, uploaded_files.filename)

    
    global FILE_PATH
    FILE_PATH = big_size.main(src, compN, template)
    return('ok')

@app.route("/bigsizeNames", methods = ['POST'])
def do_big_names():
    uploaded_files = request.files['file']
    uploaded_files.save(os.path.join(UPLOAD_FOLDER, uploaded_files.filename))
    compN = request.form['compN']
    date = request.form['date']
    template = request.form['template']
  
    global FILE_PATH    
    FILE_PATH = big_size_names.main(compN, os.path.join(UPLOAD_FOLDER, uploaded_files.filename), template, date)
    return('ok')

@app.route('/smallsize', methods=['POST'])
def do_small():
    uploaded_array = request.form['names']
    compN = request.form['compN']
    color = request.form['color']
    uploaded_array = uploaded_array.split('\n')
    cleaned_array = [s.replace('\r', '') for s in uploaded_array]
    print(cleaned_array, compN, color)

    
    global FILE_PATH
    FILE_PATH = small_size_new.main(cleaned_array, compN, color)
    return('ok')
#sends generated file to frontend
@app.route("/download", methods = ['GET'])
def download():
    print('file is being downloaded, path: ', FILE_PATH)
    return send_file(FILE_PATH, mimetype='application/pdf', as_attachment=True)

if __name__ == "__main__":
    app.run("localhost", 6969, debug = True)

#hello = input("press enter to terminate")