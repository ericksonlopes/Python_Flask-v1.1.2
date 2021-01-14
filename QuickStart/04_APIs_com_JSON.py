from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/me')
def me_api():
    return {
        "username": 'Erickson',
        "idade": 18
    }


@app.route('/user')
def user_api():
    return jsonify([1, 2, 4, 3, 5])

app.run()