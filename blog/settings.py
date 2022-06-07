import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

BIND_KEY = 'db_debug'

if BIND_KEY == 'db_prod':
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_PROD')
else:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_DEBUG')

SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
SECRET_KEY = os.urandom(32)

SQLALCHEMY_BINDS = {
    'db_debug': SQLALCHEMY_DATABASE_URI,
    'db_prod': SQLALCHEMY_DATABASE_URI
}
