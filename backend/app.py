from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/Remine')
def display():
    return render_template('example.html')

if __name__=='__main__':
    app.run(debug = True, host = '0.0.0.0',port=1234)
