from flask import Flask, request, make_response, url_for, redirect, send_file, render_template
from flask_cors import CORS
import os
import big_size

app = Flask(__name__)
CORS(app)


UPLOAD_FOLDER = r'C:\Users\arsen\proga\nametags_maker\uploaded'


@app.route("/downloads")
def file_downloads():
    try:
        return render_template('downloads.html')
    except Exception as ex:
        return str(ex)

@app.route("/test", methods = ['POST', 'GET'])
def hello():
    if request.method == 'GET':
        return {
            "one":[ "one", "two"],
            "two": "two"
        }

@app.route("/data", methods = ['POST', 'GET'])
def data():
    if request.method == 'POST':
        test = request.form
        uploaded_files = request.files['file']
        uploaded_files.save(os.path.join(UPLOAD_FOLDER, uploaded_files.filename))
        src = os.path.join(UPLOAD_FOLDER, uploaded_files.filename)

        if 'compN' not in request.form:
            compN = 'default'
        else: compN = request.form['compN']
    
        if 'template' not in request.form:
            template = 'bg_1.png'
        else: template = request.form['template']
        
        print(test)
        print(compN, uploaded_files, template)
        global FILE_PATH 
        FILE_PATH = big_size.main(src, compN, template)
        
       
        
        return send_file(FILE_PATH, as_attachment=True)
    
    return 'get?' 

@app.route("/download", methods = ['GET'])
def download():
    print('file is being downloaded, path: ', FILE_PATH)
    return send_file(FILE_PATH, mimetype='application/pdf', as_attachment=True)

if __name__ == "__main__":
    app.run("localhost", 6969, debug = True)