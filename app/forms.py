from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,TextField,validators
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class ConfigForm(Form): 

    region=TextField('Enter a region:', [validators.Required(),validators.Length(min=3, max=25)])
    bucket=TextField('S3 Folder Name:', [validators.Required(),validators.Length(min=4, max=25)])
    s3key=StringField('S3 Key Name:',[validators.Required()])
    s3user=TextField('S3 User Name:', [validators.Required(),validators.Length(min=4, max=100)])
    avldb=TextField('AVL DB Name:', [validators.Required(),validators.Length(min=4, max=25)])
    avluserid=TextField('AVL User ID:', [validators.Required(),validators.Length(min=4, max=25)])
    avlpasswd=TextField('AVL Password:', [validators.Required(),validators.Length(min=4, max=25)])
    ec2pubkey=TextField('EC2 key file name:', [validators.Required(),validators.Length(min=4, max=25)])

class BIData(Form):

    num_of_fleet=IntegerField('The number of fleets that were refreshed:')
    last_refresh=DateField('Date Of Last Refresh:')
    comments=TextAreaField('Comments:')

    





