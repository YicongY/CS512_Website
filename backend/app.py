from flask import Flask,request,render_template
import subprocess
from subprocess import Popen,PIPE
app = Flask(__name__)

@app.route('/')
def render():
    return render_template('example.html')

@app.route('/C')
def runC():
    subprocess.call(['make', '-C', '../c++'])
    process =Popen(['./../c++/q1'],stdout = PIPE,stderr = PIPE)
    stdout,stderr = process.communicate()
    return stdout

if __name__=='__main__':
    app.run(debug = True, host = '0.0.0.0',port=1111)
    #app.run(debug = True,host = '0.0.0.0')
