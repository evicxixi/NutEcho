from flask import Blueprint, redirect, render_template, send_file, request
from flask import jsonify
from service import mongodb
import settings
from settings import RET
import os
from bson.json_util import dumps
import json
import bson

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
    print('/echo_add > data', type(data), data)

    # 校验并获取user数据
    db, collection = mongodb.get_db_client(settings.DB, 'user')
    user_obj = mongodb.find_one(collection, field='_id',
                                value=data.get('user_id'))
    if user_obj.get('password'):
        user_obj.pop('password')    # pop掉敏感数据password
    if user_obj.get('echo_list'):
        user_obj.pop('echo_list')    # pop掉无用数据echo_list
    user_obj['user_remark'] = data.get('user_remark')
    print('user_obj', user_obj)

    if not user_obj:    # 若当前user异常
        RET['code'] = -1
        RET['msg'] = '绑定失败，用户不存在！'
        return jsonify(RET)

    print('1.------------')
    # 1. 向echo数据库添加当前echo数据 并添加user_list（用户列表）
    # 校验并获取当前echo数据（echo_obj说明此设备已经被绑定用户）
    db, collection = mongodb.get_db_client(settings.DB, 'echo')
    echo_obj = mongodb.find_one(collection, field='serial',
                                value=data.get('serial'))

    print('1.1------------')
    if not echo_obj:    # 1.1 若设备未绑定 向echo数据库插入当前echo数据
        data['user_list'] = []
        collection.insert_one(data)  # 向echo数据库中插入当前echo数据（含空的user_list）

    # 若设备已绑定
    echo_obj = mongodb.find_one(collection, field='serial',
                                value=data.get('serial'))

    # 构造当前echo绑定的所有user的_id的list
    user_id_list = echo_obj.get('user_list')
    user_id_list = [str(user['_id']) for user in user_id_list]
    print('user_id_list', user_id_list)

    if data.get('user_id') in user_id_list:    # 若当前user已在当前echo设备的user_list中
        RET['code'] = -2
        RET['msg'] = '您已绑定过此echo设备!'
        return jsonify(RET)

    print('1.2------------')
    # 1.2 在当前echo的user_lis字段插入新user
    collection.update_one({'serial': data['serial']}, {
        "$push": {'user_list': user_obj}})

    print('2.--------------------------------')
    # 2. 向当前user数据库添加echo_list数据
    # 2.1 构造当前user绑定的echo列表

    # 当前待绑定的echo数据中pop掉无用数据
    del echo_obj['user_list']
    if echo_obj.get('user_id'):
        echo_obj.pop('user_id')
    if echo_obj.get('user_remark'):
        echo_obj.pop('user_remark')
    print('echo_obj 当前待绑定的echo数据中pop掉无用数据', type(echo_obj), echo_obj)

    # 2.2 更新user的echo_list
    db, collection = mongodb.get_db_client(settings.DB, 'user')
    collection.update_one({'_id': bson.ObjectId(data['user_id'])}, {
                          '$push': {'echo_list': echo_obj}})

    RET['code'] = 1
    RET['msg'] = '绑定成功!'
    return jsonify(RET)


@im.route('/echo_list', methods=["POST", "GET"])
def echo_list():
    '''
    1. 绑定echo设备并到用户。

    '''
    data = request.json
    # print('data', type(data), data)

    # 查询当前user数据
    db, collection = mongodb.get_db_client(settings.DB, 'user')
    user_obj = mongodb.find_one(
        collection, field='_id', value=data.get('_id'))
    # print('echo_list > user_obj', type(user_obj), user_obj)

    # 从当前user数据中提取echo_list数据
    echo_list = user_obj.get('echo_list')
    # print('echo_list > echo_list', type(echo_list), echo_list)

    RET['data'] = echo_list
    RET['code'] = 1
    RET['msg'] = 'ok'

    return jsonify(RET)
