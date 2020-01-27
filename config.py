import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'[\xffv\xcf\xd2\x8b:7\x88V\xc8\xce/\x18m\xd3'

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }


    