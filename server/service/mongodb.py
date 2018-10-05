from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import jsonify
from bson.json_util import dumps
import json


def get_db_client(db, collection):
    '''
    创建一个数据库连接并指定collection
    返回 db对象 & collection对象
    '''
    client = MongoClient('localhost', 27017)  # 连接MongoDB
    db = client[db]  # 使用指定数据库
    collection = db[collection]  # 使用指定collection
    return db, collection


def find_one(collection, field=None, value=None):
    '''
    查找是否存在指定用户
    '''
    # id = '123456777777123456777777'
    field = str(field)
    if field == '_id':
        data = collection.find_one({'_id': ObjectId(value)})
    else:
        data = collection.find_one({field: value})
    if data:
        data = dict(data)
        data['_id'] = str(data.get('_id'))
    else:
        data = ''
    return data


def find_all(collection):
    '''
    获取数据表中所有数据并转换为list
    '''

    data = collection.find()    # 此时返回的是一个Cursor object 不能被 serializable
    data = dumps(data)
    data = json.loads(data)

    for index, item in enumerate(data):
        data[index]["_id"] = str(item.get("_id"))
    # print('data', type(data), data)

    return jsonify(data)


def insert_one(collection, data):
    '''
    在指定MongoDB的collection中插入一条数据
    '''
    collection.insert_one(data)
    return True


def insert_many(collection, data):
    '''
    获取数据表中所有数据并转换为list
    '''

    # print('insert_many > data 1', type(data), data)
    data = collection.insert_many(data)
    # print('insert_many > data', type(data), data)

    # return jsonify(data)
    return data
