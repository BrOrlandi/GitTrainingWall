from flask import Flask
from flask.templating import render_template
import os

app = Flask(__name__)


def list_users():
    users = os.listdir('./templates/users')
    return users


@app.route('/')
def index():
    return render_template('index.html', users=list_users(), script=True)


@app.route('/users')
def get_users():
    return '%d' % len(list_users())

# foi necessário mudar o estilo da porta para rodar
if __name__ == '__main__':
    app.run('localhost',5000)
