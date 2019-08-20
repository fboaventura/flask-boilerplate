#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Flask + Python3 application template
Author: Frederico Freire Boaventura <frederico@boaventura.net>
URL: https://gitlab.com/ffb-portfolio/websites/flask-boilerplate
     https://github.com/fboaventura/flask-boilerplate
Licence: GPLv3
"""

from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, DateTimeField, PasswordField
from wtforms.validators import Required
from flask_babel import _, lazy_gettext as _l


class ExampleForm(FlaskForm):
    title = TextField(_l('Subject'), validators=[Required()])
    content = TextAreaField(_l('Text'))
    date = DateTimeField(_l('Date'), format='%d/%m/%Y %H:%M')
# recaptcha = RecaptchaField(_('Recaptcha'))
