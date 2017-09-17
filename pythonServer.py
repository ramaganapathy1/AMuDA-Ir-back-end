from flask import Flask, session, redirect, url_for
from flask import request  # getting post request
from flask import render_template
from pymongo import MongoClient
import os
client = MongoClient('mongodb://localhost:27017/')
db = client.ir
app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route('/', methods=['GET'])
def index():
    if 'name' not in session or session['name']=='':
        return render_template('index.html')
    else:
        li = []
        li = session
        print ('li',li)
        return render_template('index.html', user=li)


@app.route('/signUp', methods=['POST'])
def signup():
    if request.method == 'POST':
        post_data = {}
        post_data['_id'] = request.form['number']
        post_data['name'] = request.form['name']
        post_data['gender'] = 'male'
        post_data['email'] = request.form['email']
        post_data['number'] = request.form['number']
        post_data['password'] = request.form['password']
        print (post_data)
        try:
            db.user.insert_one(post_data)
            print ("done")
            return redirect(url_for('index'), code=200)
        except:
            print ("wrong")
            return redirect(url_for('index'), code=400)

@app.route('/dashboard',methods=['GET'])
def dashboard():
    return render_template('dashboard.html')
@app.route('/signIn', methods=['POST'])
def signin():
    if request.method == 'POST':
        number = request.form['number']
        password = request.form['password']
        result = db.user.find_one({'_id': number})
        print (result)
        print (password)
        print (result['password'])
        flag = (str(result['password']) == str(password))
        print (flag)
        if flag:
            data = []
            data.append(result['number'])
            data.append(result['name'])
            # print (str(result['password']) == str(password))
            print ("Success")
            app.secret_key='ir'
            session['name'] = result['name']
            session['number'] = result['number']
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('index'),code=400)
@app.route('/logOut',methods=['GET'])
def logout():
    session.pop('name',None)
    session.pop('number',None)
    session.clear()
    print (session)
    print ("logout success")
    return redirect(url_for('index'))

@app.route('/addPaper',methods=['POST'])
def addPaper:
    return
if __name__ == '__main__':
    app.run()
