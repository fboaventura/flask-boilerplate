#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Flask + Python3 application template
Author: Frederico Freire Boaventura <frederico@boaventura.net>
URL: https://gitlab.com/ffb-portfolio/websites/flask-boilerplate
     https://github.com/fboaventura/flask-boilerplate
Licence: GPLv3
"""

import os
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from flask_babel import ngettext
from flask_babel import gettext as _
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    user = User.query.filter_by(email=email).first()
    
    # Check if user exists
    # take the user supplied password, hash it, and compare with the hashed password in database
    if not user or not check_password_hash(user.password, password):
        flash(_(u'Please check your login details and try again.'), 'danger')
        return redirect(url_for('auth.login'))  # if user doesn't exist or password is wrong, reload the page
    
    # if the above check passes, then proceed with user login
    login_user(user, remember=remember)
    return redirect(url_for('index'))


@auth.route('/signup')
def signup():
    return render_template('auth/signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first()  # if this returns true, then the e-mail is already in the database
    
    if user:
        flash(_(u'Email address already exists'), 'danger')
        return redirect(url_for('auth.signup'))
    
    # create new user with data provided by the form. Hash the password to save it into the database
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    
    # add new user to the database
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


# @auth.route('/new/')
# @login_required
# def new():
#     form = ExampleForm()
#     return render_template('new.html', form=form)
# 
# 
# @auth.route('/save/', methods=['GET', 'POST'])
# @login_required
# def save():
#     form = ExampleForm()
#     if form.validate_on_submit():
#         print("Saving data...")
#         print(form.title.data)
#         print(form.content.data)
#         print(form.date.data)
#         flash('Data sucessfuly saved!')
#     return render_template('new.html', form=form)
