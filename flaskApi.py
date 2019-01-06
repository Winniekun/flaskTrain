''' 
@author: weikunkun
@file:   flaskApi.py
@time:   19-1-6下午9:40
@contact: kongwiki@163.com
'''

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        some_josn = request.get_json()
        return jsonify({'you sent some json': some_josn}), 201
    else:
        return jsonify({"about": "hello world"})


@app.route('/multi/<int:num>', methods=['GET'])
def multi(num):
    return jsonify({'multi num': num*100})


if __name__ == '__main__':
    app.run(debug=True)
