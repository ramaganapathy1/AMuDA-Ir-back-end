from flask import Flask, session, redirect, url_for,send_file
from flask import request  # getting post request
from flask import render_template
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import os
import sys
client = MongoClient('mongodb://localhost:27017/')
db = client.ir
app = Flask(__name__)
@app.route('/start',methods=['GET'])
def start1():
    path=os.getcwd()
    print ("start")
    os.system('python intial.py')
    os.system('chmod 0777 start.sh')
    os.system('./start.sh')
    os.system('python keyphrase/start.py')
    print ("start")
    os.system('chmod 0777 start.sh keyphrase/keyphrase.sh')
    print ("start")
    os.system('./start.sh')
    os.system('cp '+path+'/keyphrase/output/*.tab  '+path+'/JVcode/Scripts/tabfiles/')
    os.system('cp ' + path + '/keyphrase/output/*.tab  ' + path + '/JVcode/Scripts/newtab/')
    os.system('python '+path+'/JVcode/Scripts/split.py')
    os.system('python '+path+'/JVcode/Scripts/AllScores.py')
    print (path)
    return "1"
if __name__ == '__main__':
    app.run(debug=True)