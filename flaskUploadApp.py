'''
@author  : kongweikun
@file    : flaskUploadApp.py
@time    : 18-7-20 下午3:27
@contact : kongwiki@163.com
'''
import os
from flask_dropzone import Dropzone
from flask import Flask, request, render_template

#项目根目录
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

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == "POST":
        file = request.files.get('file')
        file.save(os.path.join(app.config['UPLOADED_PATH'], file.filename))
    return render_template('baseUpload.html')


if __name__ == '__main__':
    app.run(debug=True)