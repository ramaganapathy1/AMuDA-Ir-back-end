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
#@production.route('/start',methods=['GET'])
class start():
    def start1(self):
        path=os.getcwd()
        print ("start")
        os.system('python production/intial.py')
        os.system('chmod 0777 production/start.sh')
        os.system('./production/start.sh')
        os.system('python production/keyphrase/start.py')
        print ("start")
        os.system('chmod 0777 production/keyphrase/start.sh production/keyphrase/keyphrase.sh')
        print ("start")
        os.system('./production/start.sh')
        os.system('cp '+path+'/production/keyphrase/output/*.tab  '+path+'/production/JVcode/Scripts/tabfiles/')
        os.system('cp ' + path + '/production/keyphrase/output/*.tab  ' + path + '/production/JVcode/Scripts/newtab/')
        os.system('python '+path+'/production/JVcode/Scripts/split.py')
        os.system('python '+path+'/production/JVcode/Scripts/AllScores.py')
        os.system('python '+path+'/production/JVcode/Scripts/ForClassification/cont-sep.py')
        os.system('python '+path+'/production/JVcode/Scripts/ForClassification/ela-sep.py')
        print (path)
        return "1"
"""if __name__ == '__main__':
    production.run(host="127.0.0.1",port=6000,debug=True)"""