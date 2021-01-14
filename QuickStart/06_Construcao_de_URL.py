from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return f'{escape(username)} profile'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Erick'))

# Para construir um URL para uma função específica, use a url_for()função.
# Ele aceita o nome da função como seu primeiro argumento e qualquer número de argumentos de palavra-chave,
# cada um correspondendo a uma parte variável da regra de URL. Partes variáveis desconhecidas são
# anexadas ao URL como parâmetros de consulta.

app.run()
