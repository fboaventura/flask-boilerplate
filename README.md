# Frederico's Flask App Boilerplate

**An (almost) complete Flask application template with useful plugins.**

Use this Flask boilerplate to initiate your project with some advance. The following plugins are installed, and some of them already in use:

*   [Flask-Login](https://flask-login.readthedocs.io/en/latest/) - Flask-Login provides user session management for Flask.
*   [Bootstrap-Flask](https://bootstrap-flask.readthedocs.io/en/latest/) - Ready-to-use Twitter-bootstrap for use in Flask.
*   [Flask-Uploads](https://pythonhosted.org/Flask-Uploads/) - Flask-Uploads allows your application to flexibly and efficiently handle file uploading and serving the uploaded files.
*   [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) - Adds cache support to your Flask application.
*   [Flask-Compress](https://github.com/colour-science/flask-compress) - allows you to compress your Flask application's responses with gzip easily.
*   [Flask-Admin](https://flask-admin.readthedocs.io/en/latest) - Flask extension module that provides an admin interface
*   [Flask-Flatpages](https://pythonhosted.org/Flask-FlatPages) - Provides flat, static pages to a Flask application on text files as opposed to a relational database.
*   [Flask-Gravatar](https://pythonhosted.org/Flask-Gravatar) - Small extension for Flask to make using Gravatar easy.
*   [Flask-Mail](https://pythonhosted.org/Flask-Mail) - Makes sending mails from Flask applications straightforward and has support for unittesting.
*   [Flask-Restless](https://flask-restless.readthedocs.io/en/stable/) - Flask-Restless provides a simple generation of ReSTful APIs for database models defined using Flask-SQLAlchemy.
*   [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) - Adds SQLAlchemy support to Flask. Quick and easy.
*   [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest) - Add PyMongo Support MongoDB.
*   [Flask-WTF](https://flask-wtf.readthedocs.io) - Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA.
*   [Flask-Themes](https://pythonhosted.org/Flask-Themes/) makes it easy for your application to support a wide range of appearances.

## Requirements 

These packages are Ubuntu related: `gcc`, `make`, `python3` (3.6+), `python3-pip`, `python3-venv`

## Instalation

First, clone this repository.

```(bash)
    $ git clone https://gitlab.com/ffb-portfolio/websites/flask-boilerplate.git
    $ cd flask-boilerplate
```

Create a virtualenv, activate and install the requirements:

```(bash)
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install --upgrade pip
    $ pip install -r requirements.txt
```

Or simply:

```(bash)
    $ make venv
```

Then, run the application:

```(bash)
    $ FLASK_APP=run.py python run.py
```

Or simply:

```(bash)
    $ make run.py
```

To see your application, access this URL in your browser:

    http://localhost:5000

All configuration options are in: [config.py](config.py)
