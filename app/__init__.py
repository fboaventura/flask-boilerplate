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
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_gravatar import Gravatar
from flask_bootstrap import Bootstrap
from flask_babel import Babel, lazy_gettext as _l
from config import Config

db = SQLAlchemy()  # flask-sqlalchemy
migrate = Migrate()  # flask-migrate
login = LoginManager()  # flask-login
login.login_view = 'auth.login'
login.login_message = _l('Please login to access this page.')
mail = Mail()
moment = Moment()
gravatar = Gravatar(
    app=None, 
    size=100,
    rating='g',
    default='robohash',
    force_default=False,
    force_lower=False,
    use_ssl=True,
    base_url=None
)
bootstrap = Bootstrap()  # flask-bootstrap
babel = Babel()  # flask-babel


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    gravatar.init_app(app)
    bootstrap.init_app(app)
    babel.init_app(app)

    from app.auth import bp as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import bp as main_blueprint
    app.register_blueprint(main_blueprint)

    if not app.debug and not app.testing:
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'],
                        app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'], subject='{} Failure'.format(current_app.config.APP_NAME),
                credentials=auth, secure=secure)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/app.log',
                                           maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('{} startup'.format(current_app.config.APP_NAME))

    return app


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])