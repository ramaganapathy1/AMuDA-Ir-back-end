from flask import Flask
from flask import request #getting post request
from flask import render_template
import json
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db=client.ir

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signUp',methods=['POST'])
def user():
    if request.method =='POST':
        post_data={}
        post_data['_id']=request.number
        post_data['name']=request.name
        post_data['gender']='male'
        post_data['email']=request.email
        post_data['number']=request.number
        print (post_data)
       # result=db.user.insert_one(post_data)
#        print (result)


if __name__ == '__main__':
    app.run()
