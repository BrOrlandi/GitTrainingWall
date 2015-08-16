from flask import Flask
from flask.helpers import url_for
from flask.templating import render_template
import os

app = Flask(__name__)

    
def list_users():
    users = os.listdir('./templates/users')
    return users

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/')
def index():
    return render_template('index.html',users=list_users())

@app.route('/users')
def get_users():
    return '%d'%len(list_users())

if __name__ == '__main__':
    app.run(host='0.0.0.0')