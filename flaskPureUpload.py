"""
@time : 2019/12/27下午6:26
@Author: kongwiki
@File: flaskPureUpload.py
@Email: kongwiki@163.com
"""
import os
import pathlib
from flask import Flask, request, render_template, url_for, send_from_directory
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'pdf', 'gif'])

# path = pathlib.Path(os.getcwd())
# UPLOAD_FOLDER = path/'upImage'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./upImage"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>图片上传</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=file>
         <input type=submit value=上传>
    </form>
    '''


# 判断是否是符合要求的文件
def allowed_file(filename):
	return '.' in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS


@app.route("/uploads/<filename>")
def uploaded_file(filename):
	return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/", methods=["GET", "POST"])
def upload_file():
	if request.method == "POST":
		file = request.files['file']
		print("文件为{} 文件名为 {}".format(file, file.filename))
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			# filename = file.filename.split(".")[0]
			print(filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			file_url = url_for('uploaded_file', filename=filename)
			print("文件的路径为 {}".format(file_url))
			return html + "<br><img src=" + file_url + ">"
	return html


def unit_test():
	filename = 'wkkk.png.aaa.bbb.ccav'
	name = filename.rsplit('.', 1)
	result = "." in filename and name[1] in ALLOWED_EXTENSIONS


if __name__ == '__main__':
	app.run(debug=True)
# unit_test()
