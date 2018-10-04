import requests
import json
import mongodb
import os
import uuid
import time
# import settings

COLLECTION = 'content'


def content_save(content_url, content_id, type=None):
    '''
    根据指定的资源url 及指定的存储路径 将资源存盘
    '''
    try:    # 部分资源无cover_path 故进行错误处理
        # 对audio & cover 分别进行path拼接
        if type in ['mp3', 'wma']:
            save_path = 'audio/' + content_id + '.mp3'
        elif type in ['jpg', 'png']:
            save_path = 'cover/' + content_id + '.jpg'
        save_path = os.path.join(
            os.path.abspath(".."),
            save_path
        )
        # 资源存库
        content = requests.get(content_url).content
        with open(save_path, 'wb') as f:
            f.write(content)
    except Exception as e:
        print(e)


def get_content(content_id):
    '''
    根据指定喜马拉雅的资源id 将资源存盘及存库
    '''
    # 拼接资源url content_id = '21017396'
    content_url = 'http://m.ximalaya.com/tracks/' + content_id + '.json'

    # 获取资源所有字段
    content = requests.get(content_url).content
    content_dict = json.loads(content)

    # 生成资源唯一id
    content_id = str(uuid.uuid4())

    # 存盘（audio）
    audio_url = content_dict.get('play_path_64')
    content_save(audio_url, content_id, type='mp3')

    # 存盘（cover）
    cover_url = content_dict.get('cover_url')
    content_save(cover_url, content_id, type='jpg')

    # 资源存库
    # db, collection = mongodb.get_db_client(settings.DB, COLLECTION)
    db, collection = mongodb.get_db_client('nutapp', COLLECTION)
    data = {
        'content_id': content_id,
        'title': content_dict.get('title'),
        'category_name': content_dict.get('category_name'),
        'author': content_dict.get('nickname'),
    }
    mongodb.insert_one(collection, data)


# 资源搜集（音乐id）
song = ['21019227', '3724133', '3760263', '3772939']
for content_id in song:
    print('正在搜集资源（content_id）', content_id)
    get_content(content_id)
    time.sleep(2)
