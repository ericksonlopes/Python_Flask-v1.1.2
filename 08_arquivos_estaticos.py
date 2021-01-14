from flask import render_template, Flask, request

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('08_hello.html', name=name)


# O Flask procurará modelos na templates pasta. Portanto, se seu aplicativo é um módulo,
# esta pasta está ao lado desse módulo, se for um pacote, ela está realmente dentro do seu pacote:


app.run()
