from wat import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), nullable=False, unique=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    doing_now = db.Column(db.String, nullable=False)
    doing_later = db.Column(db.String, nullable=False)
    not_doing = db.Column(db.String, nullable=False)

    @property
    def name(self):
        return '%s %s' % (self.first_name, self.last_name)

class Status(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id), nullable=False, primary_key=True)
    timestamp = db.Column(db.DateTime, primary_key=True)
    doing_now = db.Column(db.String, nullable=False)
    doing_later = db.Column(db.String, nullable=False)
    not_doing = db.Column(db.String, nullable=False)
