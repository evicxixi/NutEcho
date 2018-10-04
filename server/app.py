from flask import Flask, render_template, request, send_file
from flask import jsonify
from service import mongodb
import settings
import bson
from blueprint import collector, im

from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket

# cors 跨域访问
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)  # cors 跨域访问
app.SECRET_KEY = 'asdfghjkl'
app.debug = True

app.register_blueprint(collector.collector, url_prefix='/API/')    # 注册蓝图
app.register_blueprint(im.im, url_prefix='/API/')    # 注册蓝图


@app.route('/')
def index():
    # return 'Hello World!'
    return render_template('echo.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    若登陆成功 返回成功消息
    若失败 返回错误信息
    '''

    # username = request.values.getlist('username')[0]
    # password = request.values.getlist('password')[0]
    username = request.json['username']
    password = request.json['password']
    print(username, password)

    db, collection = mongodb.get_db_client(
        settings.DB, settings.COLLECTION)    # 获取db.collection对象
    user_obj = mongodb.find_one(collection, field='username', value=username)
    # print('user_obj', type(user_obj), user_obj)

    if not user_obj:
        data = {
            'username': None,
            'nickname': None,
            'msg': '登录失败 用户名不存在！',
            'code': -2,
        }
    else:
        if not password == user_obj.get('password'):
            data = {
                'username': user_obj.get('username'),
                'nickname': user_obj.get('nickname'),
                'msg': '登录失败 密码错误！',
                'code': -1,
            }
        elif password == user_obj.get('password'):
            data = {
                'username': user_obj.get('username'),
                'nickname': user_obj.get('nickname'),
                'msg': '登录成功！',
                'code': 1,
            }
    return jsonify(data)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    '''
    若用户名不冲突 存库并返回注册成功信息
    若冲突 返回错误信息
    '''
    # print('request', request)
    # print('request.headers', request.headers)
    # print('request.json', type(request.json), request.json)
    # print('request.values', request.values)
    # print('request.form', request.form)

    username = request.json['username']
    password = request.json['password']
    nickname = request.json['nickname']
    gender = request.json['gender']
    # username = request.values.getlist('username')[0]
    data = {
        'username': username,
        'password': password,
        'nickname': nickname,
        'gender': gender,
    }

    db, collection = mongodb.get_db_client(
        settings.DB, settings.COLLECTION)    # 获取db.collection对象
    user_obj = mongodb.find_one(collection, {'username': username, })
    print('user_obj', user_obj)
    if user_obj:
        data = {
            'nickname': nickname,
            'msg': '用户名已存在！',
            'code': -1,
        }
    else:
        mongodb.insert_one(collection, data)    # 存库
        data = {
            'nickname': nickname,
            'msg': '注册成功！',
            'code': 1,
        }
    return jsonify(data)


@app.route('/user_info', methods=['GET', 'POST'])
def user_info():
    print('----------->')
    username = request.values.getlist('username')[0]
    db, collection = mongodb.get_db_client(
        settings.DB, settings.COLLECTION)    # 获取db.collection对象
    data = mongodb.find_one(collection, field='username', value=username)
    data['_id'] = str(data['_id'])
    print('data', data, type(data))
    return jsonify(data)
    # return data


if __name__ == '__main__':
    # app.run("0.0.0.0", 5000, debug=True)

    # 建立socket的server端
    ws_server = WSGIServer(("0.0.0.0", 5000), app,
                           handler_class=WebSocketHandler)
    ws_server.serve_forever()
