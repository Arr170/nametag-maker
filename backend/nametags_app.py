from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

ALLOWED_EXTENCIONS = {'docx'}
UPLOAD_FOLDER = r'backend\uploads'

#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
        #if 'file' not in request.files:
            #return 'u are fucked my man'
        wtf = request.files['file']
        t = request.content_type
        wtf.save(wtf.filename)
        #wtf = type(wtf)
        #wtf = open(wtf)
        print(t)
        
        
        #file = request.files
        #file.save(file.filename)
        #file.save(file.filename)
        
        return 'ok'
    
    return 200, 

    
if __name__ == "__main__":
    app.run("localhost", 6969, debug = True)