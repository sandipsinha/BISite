from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from database import init_db,db_session
from forms import LoginForm,ConfigForm
from models import User,ConfigData
import config as CONFIG
import MySQLdb.cursors
from sqlalchemy.sql import select



@app.route('/')
@app.route('/index')
@login_required
def index():
    s=select([bidetails])
    cnx = MySQLdb.connect(**CONFIG.DATABASE)
    cur=cnx.cursor(MySQLdb.cursors.DictCursor)
    result=cur.execute(s)
        
    #user = g.user
    #posts = [  # fake array of posts
    #    { 
    #        'author': {'nickname': 'John'}, 
    #        'body': 'Beautiful day in Portland!' 
    #    },
    #    { 
    #        'author': {'nickname': 'Susan'}, 
    #        'body': 'The Avengers movie was so cool!' 
    #    }
    #]
    #return render_template("index.html",
    #                       title='Home',
    #                       user=user,
    #                       posts=posts)

@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/config', methods=['GET', 'POST'])
@oid.loginhandler
def config():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = ConfigForm(request.form)
    if request.method == 'POST' and form.validate():
        config = ConfigData(form.bucket.data, form.region.data,form.s3key.data, form.s3user.data, form.avldb.data,form.avluserid.data,form.avlpasswd.data,form.ec2pubkey.data)
        db_session.add(config)
        db_session.commit()
        flash('Config Data has been Saved')
        return redirect(url_for('index'))

    fo = open("/home/pythonautomate/Automate/automate.cfg", "w")
    cnx = MySQLdb.connect(**CONFIG.DATABASE)
    cur=cnx.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT bucket,region,s3key,avldb,avluserid,avlpasswd,ec2pubkey from configdata")
     
    for row in cur.fetchall(): 
         form.bucket.data=row['bucket']
         form.region.data=row['region']
         form.s3key.data=row['s3key']  
         form.s3user.data=row['avluserid']
         form.avldb.data=row['avldb']
         form.avluserid.data=row['avluserid']
         form.avlpasswd.data=row['avlpasswd']
         form.ec2pubkey.data=row['ec2pubkey']
    
         # form.bucket.data = str[1].translate(None, "'")+ str[2].translate(None, "'")
            
    return render_template('config.html', form=form)


