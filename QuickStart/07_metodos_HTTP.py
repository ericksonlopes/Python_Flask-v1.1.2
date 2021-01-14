# Os aplicativos da Web usam métodos HTTP diferentes ao acessar URLs.
# Você deve se familiarizar com os métodos HTTP enquanto trabalha com o Flask.
# Por padrão, uma rota responde apenas a GET solicitações. Você pode usar o method sargumento do route()
# decorador para lidar com diferentes métodos HTTP.

from flask import Flask, request

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Requisição Post'
    elif request.method == 'GET':
        return 'Requisição GET'


app.run(debug=True)
