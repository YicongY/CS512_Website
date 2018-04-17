from flask import Flask,request,render_template
from OpenSSL import SSL

context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('server.key')
context.use_certificate_file('server.crt')

app = Flask(__name__)

@app.route('/')
def render():
    return render_template('example.html')

if __name__=='__main__':
    app.run(debug = True, host = '0.0.0.0',port=1111,ssl_context=context)
