from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index page, <strong>Iniciando em Flask</strong>'


# Use o route() decorador para vincular uma função a um URL
@app.route('/hello')
def hello():
    return 'Hello, World'


app.run()
