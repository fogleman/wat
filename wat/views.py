from flask import render_template, flash, redirect, url_for
from forms import UserForm, StatusForm
from models import User
from wat import app, db
import datetime

@app.route('/')
def index():
    users = User.query.order_by(db.desc(User.timestamp)).all()
    return render_template('index.html', users=users)

@app.route('/user/list')
def user_list():
    users = User.query.order_by(User.email).all()
    return render_template('user/list.html', users=users)

@app.route('/user/create', methods=['GET', 'POST'])
def user_create():
    form = UserForm()
    if form.validate_on_submit():
        user = User(
            timestamp=datetime.datetime.utcnow(),
            doing_now='',
            doing_later='',
            not_doing='',
        )
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        flash('Successfully created user: %s' % user.name)
        return redirect(url_for('user_list'))
    return render_template('user/create.html', form=form)

@app.route('/user/<int:user_id>/status', methods=['GET', 'POST'])
def user_status(user_id):
    user = User.query.get_or_404(user_id)
    form = StatusForm(obj=user)
    if form.validate_on_submit():
        user.timestamp = datetime.datetime.utcnow()
        form.populate_obj(user)
        db.session.commit()
        flash('Successfully updated status for user: %s' % user.name)
        return redirect(url_for('index'))
    return render_template('user/status.html', form=form)
