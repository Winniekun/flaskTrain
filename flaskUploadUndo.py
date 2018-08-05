'''
@author  : kongweikun
@file    : flaskUploadUndo.py
@time    : 18-8-5 下午5:42
@contact : kongwiki@163.com
'''
from flask import Flask,render_template,request
from flask_dropzone import Dropzone

import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'upImage'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=30,
)

dropzone = Dropzone(app)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        file.save(os.path.join(app.config['UPLOADED_PATH'],file.filename))
    return render_template('undoUpload.html')

if __name__ == '__main__':
    app.run(debug=True)