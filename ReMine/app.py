from flask import Flask,request,render_template,jsonify
import subprocess
from subprocess import Popen,PIPE
#from flask_cors import CORS, cross_origin

app = Flask(__name__)
#cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def render():
    return render_template('example.html')

@app.route('/C')
def runC():
    subprocess.call(['make', '-C', '../c++'])
    process =Popen(['./../c++/q1'],stdout = PIPE,stderr = PIPE)
    stdout,stderr = process.communicate()
    return stdout
@app.route('/remine', methods =['POST'])
def runRemine():
    #subprocess.call(['bash','remine-ie.sh'])
    ret = []
    with open('results_remine/remine_result.txt','r') as f:
        for line in f:
            ret.append(line)
    return jsonify({'tuple':ret})



if __name__=='__main__':
    app.run(debug = True, host = '0.0.0.0',port=1111)
    #app.run(debug = True, host = 'localhost', port=5000)
