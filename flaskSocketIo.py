"""
@author: kongwiki
@file:   flaskSocketIo.py
@time:   19-1-17下午1:21
@contact: kongwiki@163.com
"""
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('socketIo.html')


# 向客户端发送数据
@socketio.on('client_event')
def client_msg(msg):
    emit('server_response', {'data': msg['data']})


# 从客户端接受连接成功的数据
# 并返回客户端
@socketio.on('connect_event')
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})


if __name__ == '__main__':
    socketio.run(app, debug=True)
