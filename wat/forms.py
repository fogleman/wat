from flask.ext.wtf import Form
from models import User, Status
from wtforms import TextField
from wtforms.validators import Required
from wtforms.fields.html5 import EmailField

class UserForm(Form):
    email = EmailField('Email', [Required()])
    first_name = TextField('First Name', [Required()])
    last_name = TextField('Last Name', [Required()])

class StatusForm(Form):
    doing_now = TextField('What are you working on now?')
    doing_later = TextField('What will you be working on later?')
    not_doing = TextField('What are you not working on?')
