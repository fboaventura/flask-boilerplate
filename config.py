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
from dotenv import load_dotenv, dotenv_values

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
cnf = dotenv_values()


class Config(object):
    """
    Configuration base, for all environments.
    """
    APP_NAME = os.environ.get('APP_NAME', 'MyAppName')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'SUPER_SECRET_PRODUCTION_KEY')
    DEBUG = os.environ.get('DEBUG', False)
    TESTING = os.environ.get('TESTING', False)
    DB_SCHEMA = os.environ.get('DB_SCHEMA', 'sqlite')
    DB_NAME = os.environ.get('DB_NAME', 'app.db')
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_AUTH = '{}:{}'.format(DB_USERNAME, DB_PASSWORD) if DB_USERNAME else ''
    DB_HOSTNAME = os.environ.get('DB_HOSTNAME')
    DB_PORT = os.environ.get('DB_PORT', '')
    if DB_SCHEMA and DB_SCHEMA == 'sqlite':
        SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(basedir, DB_NAME))
    elif DB_SCHEMA:
        SQLALCHEMY_DATABASE_URI = '{}://{}@{}{}/{}'.format(DB_SCHEMA, DB_AUTH, DB_HOSTNAME, DB_PORT, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BOOTSTRAP_FONTAWESOME = True
    CSRF_ENABLED = True
    BABEL_DEFAULT_LOCALE = os.environ.get('LOCALE', 'en')
    LANGUAGES = os.environ.get('LANGUAGES', ['en', 'pt_BR'])
    BABEL_DEFAULT_TIMEZONE = os.environ.get('TIMEZONE', 'UTC')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'localhost')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 25))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', False)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEBUG = os.environ.get('MAIL_DEBUG', False)

# Get your reCaptcha key on: https://www.google.com/recaptcha/admin/create
# RECAPTCHA_PUBLIC_KEY = "6LffFNwSAAAAAFcWVy__EnOCsNZcG2fVHFjTBvRP"
# RECAPTCHA_PRIVATE_KEY = "6LffFNwSAAAAAO7UURCGI7qQ811SOSZlgU69rvv7"


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app_test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
