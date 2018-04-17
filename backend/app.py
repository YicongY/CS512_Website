from flask import Flask,request,render_template

import subprocess
app = Flask(__name__)

@app.route('/')
def render():
    return render_template('example.html')

@app.route('/C')
def runC():
    result = subprocess.run(['./../c++/q1'])
    return result

if __name__=='__main__':
    app.run(debug = True, host = '0.0.0.0',port=1111)
