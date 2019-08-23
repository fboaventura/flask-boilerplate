#!/usr/bin/env python3
# coding: utf-8

from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from app import db
from app.main.forms import EditProfileForm
from app.models import User
from app.main import bp


@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    g.locale = str(get_locale())


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    user = User.query.filter_by(username=current_user.username).first_or_404()
    return render_template('index.html', title=_('Home'), user=user)


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        print('form:', form)
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        current_user.name = form.name.data
        # current_user.email = form.email.data
        db.session.commit()
        flash(_('Your changes have been saved'))
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
        form.name.data = current_user.name
        # form.email.data = current_user.email

    return render_template('edit_profile.html', page_title=_('Edit Profile'), form=form)
