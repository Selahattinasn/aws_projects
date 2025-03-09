from flask import Flask
app = Flask(__name__)

@app.route('/')
def head():
     return "Hello World"

@app.route('/secondpage')
def second():
     return "This is second page!"

@app.route('/thirdpage')
def third():
     return "This is thirth page!"

@app.route('/fourth/<string:id>')
def fourt(id):
     return f'id of this page is {id}!'

if __name__ == '__main__':

     #app.run(debug=True, port=3000)
     #app.run(debug=True)
     app.run(host= '0.0.0.0', port=80)