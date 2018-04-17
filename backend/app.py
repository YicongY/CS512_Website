from flask import Flask,request,render_template

from subprocess import Popen,PIPE
app = Flask(__name__)

@app.route('/')
def render():
    return render_template('example.html')

@app.route('/C')
def runC():
    process =Popen(['.','/../c++/q1'],stdout = PIPE)
    stdout = process.communicate()
    return stdout

if __name__=='__main__':
    app.run(debug = True, host = '0.0.0.0',port=1111)
    #app.run(debug = True,host = '0.0.0.0')
