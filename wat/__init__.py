from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('wat.config')

db = SQLAlchemy(app)

import hooks
import models
import forms
import views
