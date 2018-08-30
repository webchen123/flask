from flask import Flask,render_template,request
from werkzeug import secure_filename
app = Flask(__name__)
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)
@app.route('/login',methods=['POST','GET'])
def login():
    error = None
    if request.method=='POST':
        if valid_login(request.form['username'],request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Ivalid username/password'
    return render_template('login.html',error=error)
@app.route('/upload',methods=['POST','GET'])
def upload_flie():
    if request.method=="POST":
        f = request.files['the_file']
        f.save('./static'+ secure_filename(f.filename))
def log_the_user_in(name):
    return render_template('hello.html',name=name)
def valid_login(name,password):
    if name=='abc' and password=='123':
        return True
    else:
        return False
if __name__=='__main__':
    app.run(debug = True)



