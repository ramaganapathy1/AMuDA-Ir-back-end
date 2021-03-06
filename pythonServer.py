from flask import Flask, session, redirect, url_for,send_file
from flask import request  # getting post request
from flask import render_template,jsonify
from pymongo import MongoClient
from werkzeug import secure_filename
from datetime import datetime
import thread,time
import os
go={}
client = MongoClient('mongodb://localhost:27017/')
db = client.ir
app = Flask(__name__)
app.secret_key = os.urandom(32)
UPLOAD_FOLDER = '../AMuDA-Ir-back-end/uploads'
ALLOWED_EXTENSIONS = ['pdf']
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
path=os.getcwd()
def logMaker(path):
    r=db.login.insert_one({"path":path,"user":session['number'],"time":datetime.utcnow()})
    print r,path
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
        post_data['path']=[]
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
        paper=db.papers.find({"userId":n})
        print (session['number'])
        print (paper.count())
        for i in paper:
            if i['domain'] not in li1:
                li1.append(i['domain'])
        print (li1)
        if session['name'] not in go:
            go[session['name']]=[]
        go[session['name']].append("dashboard")
        #if (session['lastpage'] == 1 and len(session['lastRead']) > 0):
        result = db.timeStamp.update({'name': session['lastRead'], 'userId': session['number']},
                                     {'$push': {'endTime': datetime.utcnow()}})
        print "End Time ",datetime.utcnow(),"----",result
        session['lastRead'] = ""
        session['lastpage'] = 0
        logMaker("dashboard")

        return render_template('dashboard.html',li=li1)
    else:
        return redirect(url_for('index'))
@app.route('/signIn', methods=['POST'])
def signin():
    if request.method == 'POST':
        number = request.form['number']
        password = request.form['password']
        result = db.user.find_one({'_id': number})
        #print ("result : ",len(result))
        flag=0
        flag = (str(result['password']) == str(password))
        print (flag)
        if flag and len(result)>0:
            data = []
            data.append(result['number'])
            data.append(result['name'])
            # print (str(result['password']) == str(password))
            print ("Success")
            month=time.strftime("%m")
            year=time.strftime("%Y")
            day=time.strftime("%d")
            db.entry.insert({"userId":number,"month":month,"year":year,"date":day})
            app.secret_key='ir'
            session['name'] = result['name']
            session['number'] = result['number']
            session['lastRead']=""
            session['lastpage']=0
            session['path']=result['path']

            c=db.papers.find({"userId":number})
            result2 = db.papers.find({'userId':number, 'status': '1'})
            session['count']=c.count()
            session['count2']=result2.count()
            rT=db.entry.find({"userId":number})
            print (rT.count())
            lirt=[]
            for i in rT:
                lirt.append(i)
            return render_template('index.html',li=lirt)
            logMaker("login")
        else:
            return redirect(url_for('index'),code=400)
@app.route('/logOut',methods=['GET'])
def logout():
    go[session['name']].append("logout")
    if(session['lastpage']==1 and len(session['lastRead'])>0):
        result = db.timeStamp.update({'name': session['lastRead'], 'userId': session['number']},
                                     {'$push': {'endTime': datetime.utcnow()}})
        session['lastRead']=""
        session['lastpage']=0
    session.pop('name',None)
    session.pop('number',None)

    session.clear()
    print (session)
    print ("logout success")
    logMaker("logout")
    return redirect(url_for('index'))

@app.route('/addPaper',methods=['GET','POST'])
def addPaper():
    if request.method =='POST' and 'name' in session:
        data = {}
        data['_id'] = request.form['name']
        data['userId'] = session['number']
        data['status'] = '0'
        f = request.files['file']
        filename = session['number']+"-"+f.filename.replace(" ","")
        data['filename'] = filename
        data['domain'] = request.form['domain']
        data['name'] = request.form['name']
        data['keywords']=""
        data['abstract']=""
        data['rCount']=0
        data['next']=[]
        data['continuation'] = []
        data['elaboration'] = []
        go[session['name']].append("paper added --- "+f.filename)
        print (data)
        print("paper added", data)
        print (f)
        print (filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        r=db.papers.insert_one(data)
        data['continuation']=[]
        data['elaboration']=[]
        r = db.rPaper.insert_one(data)

        if (session['lastpage'] == 1 and len(session['lastRead']) > 0):
            result = db.timeStamp.update({'name': session['lastRead'], 'userId': session['number']},
                                         {'$push': {'endTime': datetime.utcnow()}})
            session['lastRead'] = ""
            session['lastpage'] = 0
        print(r)
        logMaker("added paper - "+data['name'])
        return redirect(url_for('dashboard'))
    else:
        return "You are not good at hacking sorry!"
@app.route('/read/<paperName>',methods=['GET'])
def markRead(paperName):
    if 'name' in session:
        print (paperName)
        r = db.papers.update({'_id':paperName,'userId':session['number']},{ '$set' :{'status':'1'}})
        r = db.rPaper.update({'_id': paperName, 'userId': session['number']}, {'$set': {'status': '1'}})
        print (r)
        go[session['name']].append("read  --- "+paperName)
        if (session['lastpage'] == 1 and len(session['lastRead']) > 0):
            result = db.timeStamp.update({'name': session['lastRead'], 'userId': session['number']},
                                         {'$push': {'endTime': datetime.utcnow()}})
            session['lastRead'] = ""
            session['lastpage'] = 0
        if( r['nModified'] ==1):
            print(paperName+' Marker Successfully')
            return redirect(url_for('dashboard'),code=200)
            logMaker("marked read - "+paperName)
        else:
            return redirect(url_for('dashboard'),code=301)
    else:
        return redirect(url_for('index'))
@app.route('/domain/<dname>',methods=['GET'])
def domain(dname):
    if 'name' in session:
        papers = db.rPaper.find({'userId':session['number'],'domain':dname})
        li1=[]
        for i in papers:
            li1.append(i)
        print (li1)
        go[session['name']].append("domain view ---- "+ dname )
        if (session['lastpage'] == 1 and len(session['lastRead']) > 0):
            result = db.timeStamp.update({'name': session['lastRead'], 'userId': session['number']},
                                         {'$push': {'endTime': datetime.utcnow()}})
            session['lastRead'] = ""
            session['lastpage'] = 0
            logMaker("domain")
        return render_template('list.html',li=li1)
    else:
        return redirect(url_for('index'),code=400)
@app.route('/recommend/<paperName>',methods=['GET'])
def recommend(paperName):
    if('name' in session):
        result = db.rPaper.find({'_id':paperName,'userId':session['number']})
        print (result)
        li1=[]
        for i in result:
            li1.append(i)

        if (session['lastpage'] == 1 and len(session['lastRead']) > 0):
            result = db.timeStamp.update({'name': session['lastRead'], 'userId': session['number']},
                                         {'$push': {'endTime': datetime.utcnow()}})
            session['lastRead'] = ""
            session['lastpage'] = 0
            logMaker("recom - "+paperName)
        return render_template("recommend.html",li=li1)
    else:
        return( "sorry you are not good at hacking!" )
@app.route('/upload/<filename1>',methods=['GET'])
def uploads(filename1):
    print (os.path)
    if 'name' in session:
        print (filename1, "is requested")
        print ("send file : ",filename1)
        r=db.timeStamp.find({"fileName":filename1,"userId":session['number']})
        if r.count()==0:
            result = db.timeStamp.insert_one(
                {"userId": session['number'], "fileName": filename1, "startTime": [datetime.utcnow()], "endTime": []})
        else:
            result = db.timeStamp.update(
                {"userId": session['number'], "fileName": filename1},{'$push':{ "startTime": datetime.utcnow()}})
        r=db.rPaper.find_one({"userId":session['number'],"filename":filename1})
        t=r["rCount"]
        t=t+1
        r=db.rPaper.update({"userId":session['number'],"filename1":filename1},{'$set' :{"rCount":t}})
        print ("Sent : ",result)
        session['lastRead']=filename1
        print (session['lastRead'])
        go[session['name']].append("upload route --- "+filename1)
        #if (session['lastpage'] == 1 and len(session['lastRead']) > 0):
            #result = db.timeStamp.update({'name': session['lastRead'], 'userId': session['number']},
             #                            {'$push': {'endTime': datetime.utcnow()}})
            #session['lastRead'] = ""
            #session['lastpage'] = 0
        logMaker("paper read"+filename1)
        return send_file(path+'/uploads/'+filename1,as_attachment=False,attachment_filename=filename1)
    else:
        return redirect(url_for('index'),code=400)
@app.route('/end',methods=['POST'])
def end():
    if request.method=="POST":
        file=session['lastRead']
        result=db.timeStamp.update({'fileName':file,'userId':session['number']},{ '$push' :{'endTime':datetime.utcnow()}})
        session['lastRead']=""
        return redirect(url_for('dashboard'),code=200)
        go[session['name']].append("end route ----",session['lastRead'])
    else:
        return "sorry you are not good at hacking !"
@app.route('/delete/<paperName>',methods=['GET'])
def delete(paperName):
    r=db.papers.find_one({'name': paperName})
    r1=db.papers.remove({'name': paperName})
    r2=db.rPaper.remove({'name': paperName})
    r3=db.timeStamp.remove({'name': paperName})
    path=os.getcwd()

    if(session['lastpage']==1 and len(session['lastRead'])>0):
        result = db.timeStamp.update({'name': session['lastRead'], 'userId': session['number']},
                                     {'$push': {'endTime': datetime.utcnow()}})
        session['lastRead']=""
        session['lastpage']=0
    print (r)
    go[session['name']].append("delete route --- ",paperName)
    os.system("rm "+path+"/uploads/"+r['filename'])
    logMaker("deleted - "+ paperName)
    os.system("rm "+path+"/production/keyphrase/transcript/" + r['filename'][:-3]+'txt')
    print(r1,r2,r3)
    return redirect(url_for('dashboard'),code=200)
@app.route('/readPaper/<paperName>',methods=['GET'])
def readPaper(paperName):
    if request.method == 'GET':
        print(paperName)
        go[session['name']].append("readPaper ---- "+paperName)
        r2 = db.papers.find_one({'name': paperName})
        r=db.timeStamp.find({"name":paperName,"userId":session['number']})
        if r.count()==0:
            result = db.timeStamp.insert_one(
                {"userId": session['number'], "name": paperName, "startTime": [datetime.utcnow()], "endTime": []})
        else:
            result = db.timeStamp.update(
                {"userId": session['number'], "name": paperName},{'$push':{ "startTime": datetime.utcnow()}})
        r=db.rPaper.find_one({"userId":session['number'],"name":paperName})
        print (r)
       # if (session['lastpage'] == 1 and len(session['lastRead']) > 0):
        result = db.timeStamp.update({'name': session['lastRead'], 'userId': session['number']},
                                     {'$push': {'endTime': datetime.utcnow()}})
        print ("Check 1 : ",result)
        result = db.rPaper.update({'name': session['lastRead'], 'userId': session['number']},
                                     {'$push': {'next': paperName}})
        print ("Check 2 : ", result)
        session['lastRead'] = ""
        session['lastpage'] = 0
        #r3=db.recom.find_one({'_id': r2['filename'][:-3]+"pdf"})
        #print r3
        if "continuation" in r2 and r2['continuation']!="null":
            option1=r2['continuation']
            option2=["Paper1","Paper2","Paper3","Paper4"]
            option3=["Pap1","Pap2","Pap3","Pap4"]
            option4=r2['elaboration']
        else:
            option1 = []
            option2 = ["Paper1", "Paper2", "Paper3", "Paper4"]
            option3 = ["Pap1", "Pap2", "Pap3", "Pap4"]
            option4 = []
        t=r["rCount"]
        session['lastRead']=paperName
        t=t+1
        r=db.rPaper.update({"userId":session['number'],"name":paperName},{'$set' :{"rCount":t}})
        session['lastpage']=1
        print ("rCount" ,r)
        print(session)
        print (r2)
        option1new=[]
        option3new=[]
        """if len(option1)>0:
            #option1new=[]
            for i in option1:
                print i[:-4]+".pdf"
                rs=db.papers.find_one({'filename':i[:-10]+".pdf"})
                print rs
                option1new.append(rs['name'])
                print option1new
            #option3new=[]
            for i in session['path']:
                print i[:-4] + ".pdf"
                rs = db.rPaper.find_one({'filename': i[:-10] + ".pdf"})
                print rs
                option3new.append(rs['name'])
                print option1new
        r2["option1"] = option1new
        r2["option2"]=option2
        r2["option3"]=option3new"""
        logMaker("readPaper - "+paperName)
        return render_template('viewPdf.html',li=r2)
    else:
        return render_template('index.html')
@app.route('/search/<key>',methods=['GET'])
def search(key):
    r=db.rPaper.find({"userId":session['number']})
    print (r.count())
    d=[]
    for j in r:
        d.append(j)
    rs=[]
    print (d)
    if(session['lastpage']==1 and len(session['lastRead'])>0):
        result = db.timeStamp.update({'name': session['lastRead'], 'userId': session['number']},
                                     {'$push': {'endTime': datetime.utcnow()}})
        session['lastRead']=""
        session['lastpage']=0

    for i in range(0,len(d)):
        k=d[i]['keywords']
        k=k.split(",")
        if(key in k):
            rs.append(d[i])
    return render_template("search.html",li=rs)
@app.route('/index2',methods=['GET'])
def index2():
    if 'name' in session:
        go[session['name']].append("index 2 ")
        rT = db.entry.find({"userId": session['number']})
        print (rT.count())
        lirt = []
        for i in rT:
            lirt.append(i)
        print session
        if (session['lastpage'] == 1 and len(session['lastRead']) > 0):
            result = db.timeStamp.update({'name': session['lastRead'], 'userId': session['number']},
                                         {'$push': {'endTime': datetime.utcnow()}})
            session['lastRead'] = ""
            session['lastpage'] = 0
        print session
        return render_template('index.html', li=lirt)
    else:
        return redirect(url_for('index'),code=300)
@app.route('/send')
def send():
    s=""
    for i in go:
        s=s+"<br> Name : "+i
        for j in go[i]:
            s=s+"------ "+j+"<br>"
        s=s+"<br>"
    return s
if __name__ == '__main__':
    app.run()
