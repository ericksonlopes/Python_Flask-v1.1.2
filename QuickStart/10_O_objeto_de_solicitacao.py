from flask import request, Flask, render_template

app = Flask(__name__)


def valid_login(username, password):
    print(username, password)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return 'Usuario logado'
        else:
            error = 'Inalid username/password'

        return render_template('10_login.html', error=error)

    elif request.method == 'GET':
        return render_template('10_login.html')


app.run(debug=True)
