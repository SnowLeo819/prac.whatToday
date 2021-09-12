<<<<<<< HEAD
from flask import Flask, render_template
app = Flask(__name__)

## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.

@app.route('/')
def home():
   return render_template('main.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
=======
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)



@app.route('/', methods=['GET'])
def home():
    return render_template('main.html')

@app.route('/aboutus', methods=['GET'])
def aboutus():
    return render_template('aboutus.html')



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True, use_reloader=False)
>>>>>>> d866cb09c5a4afb04e64b20004d17bdef61eef53
