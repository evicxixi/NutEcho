import os

# MongoDB相关
DB = 'nutapp'
COLLECTION = 'user'


ROOT_PATH = os.path.abspath(".")
AUDIO_PATH = os.path.join(ROOT_PATH, 'audio/')
COVER_PATH = os.path.join(ROOT_PATH, 'cover/')

AUDIO_FORMAT = ['mp3', 'wma']
COVER_FORMAT = ['jpg', 'png']

RET = {
    'code': 0,
    'data': {},
    'msg': 'Welcome',
}
