import os
import flask
import json
from flask import Flask,request, jsonify
from flask import render_template
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

#https://ui-ux-gameproject-e70cc-default-rtdb.firebaseio.com/.json

@app.route('/users') # http://localhost:5000/zipcode/60050111
def get_users():
    response = requests.get('https://ui-ux-gameproject-e70cc-default-rtdb.firebaseio.com/.json')
    print(response)

#teste localhost
'''if __name__ == '__main__':
    app.run(debug=True)'''

#teste heroku
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
