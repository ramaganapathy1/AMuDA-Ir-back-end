from flask import Flask
from flask import request #getting post request
from flask import render_template

app = Flask(__name__)
def sendData():
    return "hello!"
@app.route('/')
def hello_world():
    ret=sendData()
    print (ret)
    arr=['rama','ganapathy']
    return render_template('hello.html',arr=arr)

@app.route('/user/<username>')
def user(username):
    return username

@app.route('/post/<int:id>')
def postId(id):
    return "%d" % id
@app.route('/hello',methods=['POST','GET'])
def hello():
    if request.method=='POST':
        return 'POST'
    else:
        return 'GET'


if __name__ == '__main__':
    app.run()
