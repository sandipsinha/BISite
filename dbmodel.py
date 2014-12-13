from app import db
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String,DateTime
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, backref

engine = create_engine('mysql+pymysql://navman:bidw@localhost/bidwflow', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    nickname = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    posts = relationship('posts', backref='Author', lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key = True)
    body = Column(String(140))
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)

class BIAnalytics(Base):
    __tablename__ = "bidetails"
    id = Column(Integer, primary_key = True)
    num_of_fleet=Column(Integer)
    last_refresh=Column(DateTime)
    comments=db.Column(db.String(100))
    
    def __init__(self, num_of_fleet, last_refresh):
        self.num_of_fleet = num_of_fleet
        self.last_refresh = last_refresh

    def __repr__(self):
        return '<Last Refreshed %r>' % self.last_refresh

class ConfigData(Base):
    __tablename__ = "configdata"
    id = Column(Integer, primary_key = True)
    bucket=Column(String(100))
    region=Column(String(30))
    s3key=db.Column(db.String(100))
    s3user=db.Column(db.String(100))
    avldb=db.Column(db.String(100))
    avluserid=db.Column(db.String(30))
    avlpasswd=db.Column(db.String(50))
    ec2pubkey=db.Column(db.String(50))
    
    def __repr__(self):
        return '<Region where this applies to %r>' % self.region

Base.metadata.create_all(engine)
 
    
