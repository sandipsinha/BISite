from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

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

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)

class BIAnalytics(db.Model):
    __tablename__ = 'bidetails'
    id = db.Column(db.Integer, primary_key = True)
    num_of_fleet=db.Column(db.Integer)
    last_refresh=db.Column(db.DateTime)
    comments=db.Column(db.String(100))
    
    def __init__(self, num_of_fleet=None, last_refresh=None,comments=None):
        self.num_of_fleet = num_of_fleet
        self.last_refresh = last_refresh
        self.comments=comments

    def __repr__(self):
        return '<Last Refreshed %r>' % self.last_refresh

class ConfigData(db.Model):
    __tablename__ = 'configdata'
    id = db.Column(db.Integer, primary_key = True)
    bucket=db.Column(db.String(100))
    region=db.Column(db.String(30))
    s3key=db.Column(db.String(100))
    s3user=db.Column(db.String(100))
    avldb=db.Column(db.String(100))
    avluserid=db.Column(db.String(30))
    avlpasswd=db.Column(db.String(50))
    ec2pubkey=db.Column(db.String(50))
    
    def __repr__(self):
        return '<Region where this applies to %r>' % self.region

    def __init__(self, bucket=None, region=None,s3key=None, s3user=None,avldb=None,avluserid=None,avlpasswd=None,ec2pubkey=None):
        self.bucket = bucket
        self.region = region
        self.s3key=s3key
        self.s3user=s3user
        self.avldb=avldb
        self.avluserid=avluserid
        self.avlpasswd=avlpasswd
        self.ec2pubkey=ec2pubkey

 
    
