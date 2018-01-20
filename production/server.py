from flask import Flask, session, redirect, url_for,send_file
from flask import request  # getting post request
from flask import render_template
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import os
import sys
client = MongoClient('mongodb://localhost:27017/')
db = client.ir
production = Flask(__name__)
db = client.ir
app = Flask(__name__)
app.secret_key = os.urandom(32)
UPLOAD_FOLDER = '../AMuDA-Ir-back-end/uploads'
ALLOWED_EXTENSIONS = ['pdf']
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
path=os.getcwd()
#@production.route('/start',methods=['GET'])
"""class start():
    def start1(self):
        path=os.getcwd()
        print ("start")
        os.system('python intial.py')
        os.system('chmod 0777 start.sh')
        os.system('./start.sh')
        os.system('python keyphrase/start.py')
        print ("start")
        os.system('chmod 0777 keyphrase/start.sh keyphrase/keyphrase.sh')
        print ("start")
        os.system('./start.sh')
        os.system('cp '+path+'/keyphrase/output/*.tab  '+path+'/JVcode/Scripts/tabfiles/')
        os.system('cp ' + path + '/keyphrase/output/*.tab  ' + path + '/JVcode/Scripts/newtab/')
        os.system('python '+path+'/JVcode/Scripts/split.py')
        os.system('python '+path+'/JVcode/Scripts/AllScores.py')
        os.system('python '+path+'/JVcode/Scripts/ForClassification/cont-sep.py')
        os.system('python '+path+'/JVcode/Scripts/ForClassification/ela-sep.py')
        print (path)
        return "1"
s = start()
s.start1()


if __name__ == '__main__':
    production.run(host="127.0.0.1",port=6000,debug=True)"""
@app.route('/kickoff',methods=['GET'])
def kick():
    results=db.papers.find({})
    if(results.count()>=5):
        path = os.getcwd()
        print ("start")
        os.system('python intial.py')
        os.system('chmod 0777 start.sh')
        os.system('./start.sh')
        os.system('python keyphrase/start.py')
        print ("start")
        os.system('chmod 0777 keyphrase/start.sh keyphrase/keyphrase.sh')
        print ("start")
        os.system('./keyphrase/start.sh')
        os.system('cp ' + path + '/keyphrase/output/*.tab  ' + path + '/JVcode/Scripts/tabfiles/')
        os.system('cp ' + path + '/keyphrase/output/*.tab  ' + path + '/JVcode/Scripts/newtab/')
        os.system('python ' + path + '/JVcode/Scripts/split.py')
        os.system('python ' + path + '/JVcode/Scripts/AllScores.py')
        print("-----------------<Continuation>--------------------")
        #os.system('python ' + path + '/JVcode/Scripts/ForClassification/cont-sep.py')
        os.system('python ' + path + '/JVcode/Scripts/ForClassification/main.py')
        os.system('python ' + path + '/JVcode/Scripts/ForClassification/outputFiles/basePaper.py')
        print("-----------------</Continuation>--------------------")
        print("-----------------<Elaboration>--------------------")
        os.system('python ' + path + '/JVcode/Scripts/ForClassification/ela-sep.py')
        print("-----------------</Elaboration>--------------------")
        print (path)
        return ("done")
    else:
        print("No enough papers for this user : ",session['name'])
        return ("need more papers!")
if __name__ == '__main__':
    app.run()
