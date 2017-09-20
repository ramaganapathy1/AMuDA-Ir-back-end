from flask import Flask, session, redirect, url_for
from flask import request  # getting post request
from flask import render_template
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import os
client = MongoClient('mongodb://localhost:27017/')
db = client.ir
app = Flask(__name__)
app.secret_key = os.urandom(32)
UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['pdf'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def index():
    if 'name' not in session or session['name']=='':
        return render_template('index.html')
    else:
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
    if 'name' in session:
        li1=[]
        n=session['number']
        paper=db.paper.find({"user":n})
        print (session['number'])
        print (paper.count())
        for i in paper:
            li1.append(i)
        return render_template('dashboard.html',li=li1)
    else:
        return redirect(url_for('index'))
@app.route('/signIn', methods=['POST'])
def signin():
    if request.method == 'POST':
        number = request.form['number']
        password = request.form['password']
        result = db.user.find_one({'_id': number})
        print (len(result))

        # print (password)
       # print (result['password'])
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
def addPaper():

    if request.method=='POST' and 'name' in session:
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and ALLOWED_EXTENSIONS(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('dashboard',
                                    filename=filename))
        return
    else:
        return "You are not good at hacking sorry!"
if __name__ == '__main__':
    app.run()
