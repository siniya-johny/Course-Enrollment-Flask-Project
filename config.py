import os

class Config(object):
    SECRET_KEY =os.environ.get('SECRET_KEY') or b'6\xeb\x17\xa7\xd0\xac\xbb\x88cs$\xa01\x1d\x117'

    MONGODB_SETTINGS = { 'db'  : 'UTA_Enrollment' }