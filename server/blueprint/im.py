from flask import Blueprint, redirect, render_template, send_file, request
from flask import jsonify
from service import mongodb
import settings
from settings import RET
import os
from bson.json_util import dumps
import json


im = Blueprint("im", __name__)

socket_dict = {}


@im.route('/app/<id>', methods=["POST", "GET"])
def app(id):
    '''
    1. 监听并接收用户app的socket请求，并存入socket_dict。
    2. 根据请求中携带的收信人信息‘user_id’，从socket_dict中取出收信人socket。
    3. 回复‘ok’。
    '''
    app_socket = request.environ.get("wsgi.websocket")  # type:WebSocket

    if app_socket:
        socket_dict[id] = app_socket
    print('socket_dict', socket_dict)
    while True:
        msg = app_socket.receive()
        user_id = msg.get('user_id')
        other_socket = socket_dict.get(user_id)
        if other_socket:
            other_socket.send('ok')


@im.route('/echo/<id>', methods=["POST", "GET"])
def echo(id):
    '''
    1. 监听echo前端的socket请求，并存入socket_dict。
    '''

    echo_socket = request.environ.get("wsgi.websocket")  # type:WebSocket
    print('echo_socket', type(echo_socket), echo_socket)

    if echo_socket:
        socket_dict[id] = echo_socket
    print('socket_dict', socket_dict)
    while True:
        msg = echo_socket.receive()
        file_path = os.path.join(settings.ROOT_PATH, 'audio', 'auido.mp3')
        if msg:
            with open(file_path, 'wb') as fh:
                fh.write(msg)
        echo_socket.send('a5008ed0-2940-46ed-938a-109f774570a7.mp3')


@im.route("/get_content_list", methods=["POST", "GET"])
def get_content_list():
    '''
    获取content数据表中所有数据并转换为list
    '''
    db, collection = mongodb.get_db_client(settings.DB, 'content')
    data = mongodb.find_all(collection)
    # print('ok')

    return data


@im.route("/get_file/<file>", methods=["POST", "GET"])
def get_file(file):
    '''
    server端根据回答语音文件名 向前端发送文件数据流的类似接口的地址
    '''
    file_name, file_format = file.split('.')
    # print(file_name, file_format)
    if file_format in settings.AUDIO_FORMAT:
        file_path = settings.AUDIO_PATH + file_name + "." + file_format
    if file_format in settings.COVER_FORMAT:
        file_path = settings.COVER_PATH + file_name + "." + file_format
        # 若album不存在 就返回默认album
        if not os.path.exists(file_path):
            file_path = settings.COVER_PATH + 'music' + "." + file_format
    # print('file_path', file_path, type(file_path))
    return send_file(file_path)


@im.route('/verify', methods=["POST", "GET"])
def verify():
    '''
    1. 验证手机传来的对echo设备扫码验证码是否合法。
    '''
    # serial = request.values.getlist('serial')[0]

    serial = request.json['serial']
    # print('serial', type(serial), serial)

    db, collection = mongodb.get_db_client(settings.DB, 'device')
    data = mongodb.find_one(collection, field='serial', value=serial)
    if data:    # 若设备合法
        RET['code'] = 1
        RET['msg'] = '设备校验通过，感谢选购NutEcho产品！'
        RET['data'] = data
    else:        # 若设备不合法
        # mongodb.insert_one(collection, {'serial': serial})
        RET['code'] = -1
        RET['msg'] = '绑定失败，此设备设备不合法！'
        RET['data'] = data

    return jsonify(RET)


@im.route('/echo_add', methods=["POST", "GET"])
def echo_add():
    '''
    1. 绑定echo设备并到用户。
    '''

    data = request.json
    # print('data', type(data), data)

    db, collection = mongodb.get_db_client(settings.DB, 'user')
    user_obj = mongodb.find_one(collection, field='username',
                                value=data.get('master_username'))
    print('user_obj', user_obj)
    if not user_obj:
        RET['code'] = -2
        RET['msg'] = '绑定失败，用户不存在！'
        return jsonify(RET)

    db, collection = mongodb.get_db_client(settings.DB, 'echo')
    echo_obj = mongodb.find_one(
        collection, field='serial', value=data.get('serial'))
    if not echo_obj:    # 若设备未绑定
        mongodb.insert_one(collection, data)
        RET['code'] = 1
        RET['msg'] = '绑定成功'
    else:        # 若设备已绑定
        RET['code'] = -1
        RET['msg'] = '绑定失败，此设备已绑定其它用户！'

    return jsonify(RET)


@im.route('/echo_list', methods=["POST", "GET"])
def echo_list():
    '''
    1. 绑定echo设备并到用户。

    '''

    data = request.json
    # print('data', type(data), data)

    db, collection = mongodb.get_db_client(settings.DB, 'echo')
    echo_list = collection.find({'master_username': data.get('username')})

    data = list(echo_list)
    # print('data list', type(data), data)
    data = dumps(data)
    # print('dumps(data)', type(data), data)
    data = json.loads(data)
    # print('json.loads', type(data), data)
    RET['data'] = data
    RET['code'] = 1
    RET['msg'] = 'ok'

    return jsonify(RET)
    # return RET
