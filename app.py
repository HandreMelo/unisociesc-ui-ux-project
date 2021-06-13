import os
import flask
import random
import string
import json
from flask import Flask,request, jsonify
from flask import render_template
import requests

# set the project root directory as the static folder, you can set others.
app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/<game>')
def get_users(game):
    response = requests.get('https://ui-ux-gameproject-e70cc-default-rtdb.firebaseio.com/'+game+'/.json').json()
    return filterResponse(response)


def filterResponse(response):
    if (not response):
        return {}
    try:
        for id in response.keys():
            del response[id]['userEmail']
    except:
        print("Alguma chave do dicionário não existe")
        return {}
    return response
        
def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    print(result_str)
'''
#teste localhost
if __name__ == '__main__':
    app.run(debug=True)
'''
#teste heroku
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
