from flask import Flask

app = Flask(__name__)


# É semelhante a uma pasta em um sistema de arquivos. Se você acessar o URL sem uma barra final,
# o Flask redirecionará você para o URL canônico com a barra final.
@app.route('/projects/')
def projects():
    return 'The project page'


# É semelhante ao nome do caminho de um arquivo. Acessar o URL com uma barra final produz um erro 404
# “Não encontrado”. Isso ajuda a manter os URLs exclusivos para esses recursos, o que ajuda os mecanismos de
# pesquisa a evitar a indexação da mesma página duas vezes.
@app.route('/about')
def about():
    return 'The about page'


app.run()
