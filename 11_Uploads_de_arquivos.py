# Você pode lidar com arquivos carregados com o Flask facilmente. Apenas certifique-se de não esquecer de definir o
# enctype="multipart/form-data"atributo em seu formulário HTML, caso contrário, o navegador não transmitirá seus arquivo
# Os arquivos carregados são armazenados na memória ou em um local temporário no sistema de arquivos. Você
# pode acessar esses arquivos observando o filesatributo no objeto de solicitação. Cada arquivo carregado é
# armazenado nesse dicionário. Ele se comporta como um fileobjeto Python padrão , mas também possui um save()
# método que permite armazenar esse arquivo no sistema de arquivos do servidor.
# Aqui está um exemplo simples que mostra como isso funciona:

from flask import request, Flask
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))
