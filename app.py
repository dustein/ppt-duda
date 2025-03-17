from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configuração para a pasta de upload
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Crie a pasta de upload se ela não existir
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Rota para renderizar o formulário de upload
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Rota para processar o upload do arquivo
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' in request.files:
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'Arquivo enviado com sucesso!'
    return 'Nenhum arquivo enviado'

if __name__ == '__main__':
    app.run(port=8080, debug=True)
