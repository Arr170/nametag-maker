from flask import Flask, request, make_response, url_for, redirect, send_file, render_template
from flask_cors import CORS
import os
import big_size
import small_size_new

app = Flask(__name__,template_folder='templates')
CORS(app)


UPLOAD_FOLDER = r'C:\Users\arsen\proga\nametags_maker\uploaded'


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
@app.route("/bigsize", methods = ['POST', 'GET'])
def do_big():
    if request.method == 'POST':
       
        uploaded_files = request.files['file']
        uploaded_files.save(os.path.join(UPLOAD_FOLDER, uploaded_files.filename))
        src = os.path.join(UPLOAD_FOLDER, uploaded_files.filename)

        #idk, it is kinda useless if statment
        if 'compN' not in request.form:
            compN = 'default'
        else: compN = request.form['compN']
    
        if 'template' not in request.form:
            template = 'bg_1.png'
        else: template = request.form['template']
        #print(compN, uploaded_files, template)

        global FILE_PATH #global variable stores path to generated file, so another function can send it back to frontend
        FILE_PATH = big_size.main(src, compN, template)
        
       
        
        return('ok')
    
    return 'get?' 

@app.route('/smallsize', methods=['POST'])
def do_small():
    uploaded_arrey = request.form['names']
    compN = request.form['compN']
    color = request.form['color']
    uploaded_array = uploaded_arrey.split('\n')
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