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
    os.system('python keyphrase/start.py')
    os.system('chmod 0777 start.sh keyphrase/keyphrase.sh')
    os.system('bash ./start.sh')
    return "1"
if __name__ == '__main__':
    app.run(port=8000,host="ir.sigappysupreme.com",debug=True)