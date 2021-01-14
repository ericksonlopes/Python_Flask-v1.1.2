from flask import abort, redirect, Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(404)


# retorna todos que cairem no erro 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_noy_found.html'), 404


app.run()
