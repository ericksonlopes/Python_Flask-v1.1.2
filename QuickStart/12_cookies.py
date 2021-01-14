from flask import Flask, request, make_response, render_template

app = Flask(__name__)


# Lendo cookies:
@app.route('/s')
def index():
    username = request.cookies.get('username')


# Armazenamento de cookies:
@app.route('/')
def index():
    resp = make_response(render_template('08_hello.html'))
    resp.set_cookie('username', 'the username')
    return resp


app.run()
