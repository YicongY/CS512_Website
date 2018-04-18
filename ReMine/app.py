from flask import Flask,request,render_template,jsonify,Response
import subprocess
from subprocess import Popen,PIPE

from gevent.wsgi import WSGIServer

from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin(origin='*')
def render():
    return render_template('example.html')

@app.route('/C')
@cross_origin(origin='*')
def runC():
    #subprocess.call(['make', '-C', '../c++'])
    process =Popen(['./../c++/q1'],stdout = PIPE,stderr = PIPE)
    stdout,stderr = process.communicate()
    return stdout
@app.route('/remine', methods =['POST'])
@cross_origin(origin='*')
def runRemine():
    #subprocess.call(['bash','remine-ie.sh'])
    ret = []
    with open('results_remine/remine_result.txt','r') as f:
        for line in f:
            ret.append(line)
    input = request.data
    #print(input.type)
    #text = input['text']
    print(input)
    return jsonify({'tuple':ret})



if __name__=='__main__':
    #app.run(debug = True, host = '0.0.0.0',port=1111)
    http_server = WSGIServer(('0.0.0.0', 1111), app)
    http_server.serve_forever()
    #app.run(debug = True, host = 'localhost', port=5000)
