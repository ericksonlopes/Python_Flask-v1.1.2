from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/user/<username>')
def exibir_user_profile(username):
    return f'Usuário {escape(username)}'


@app.route('/post/<int:post_id>')
def exibir_post(post_id):
    return f'Post {escape(post_id)}'


app.run()
