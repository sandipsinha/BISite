import os
WTF_CSRF_ENABLED = True
 
SECRET_KEY = 'you-will-never-guess'
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://navman:bidw@localhost/bidwflow'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
DATABASE = {
         'db': 'bidwflow',
         'host': 'localhost',
         'port': 3306,
         'user': 'root',
         'passwd': 'bidw',
     }
