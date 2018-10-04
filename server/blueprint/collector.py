from flask import Blueprint, redirect, render_template, send_file, request
from flask import jsonify
import settings
import json
from service import mongodb
from bson.json_util import dumps
import os
# 可以为蓝图独立Temp 和 static    而flask实例化的时候不需要定义名称
collector = Blueprint("collector", __name__)


@collector.route("/audio_list", methods=['GET', "POST"])
def audio_list():   # 备注（坑）：蓝图注册名称，与蓝图的路由函数名称不能重复。
    '''
    提供所有audio的信息。
    '''
    db, collection = mongodb.get_db_client('nutapp', 'content')
    data = mongodb.find_all(collection)

    return data


@collector.route("/file/<type>/<id>", methods=['GET', "POST"])
def get_file(type, id):
    '''
    拼接server端的audio & cover的资源路径，发送到前端。
    '''
    type = str(type)
    content_path = type + '/' + id
    # print('content_path', content_path)

    # 若无conver_path 使用默认cover
    if not os.path.exists(content_path):
        content_path = type + '/' + 'default.jpg'

    return send_file(content_path)


@collector.route("/content_one", methods=['GET', "POST"])
def content_one():
    field = request.values.get("field")
    value = request.values.get("value")
    # print('field', type(field), field)
    # print('value', type(value), value)
    db, collection = mongodb.get_db_client('nutapp', 'content')
    data = mongodb.find_one(collection, field=field, value=value)
    # data = mongodb.find_all(collection)
    print('content_one data', data, type(data))
    # return jsonify(data)
    return data
