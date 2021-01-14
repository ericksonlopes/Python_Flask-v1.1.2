from flask import abort, redirect, Flask, url_for, render_template, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(401)


# retorna todos que cairem no erro 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_noy_found.html'), 404


# Você só precisa envolver a expressão de retorno com make_response()
# e obter o objeto de resposta para modificá-lo e retorná-lo:
@app.errorhandler(401)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp


app.run()
