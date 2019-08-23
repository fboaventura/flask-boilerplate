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
from app import create_app

# ----------------------------------------
# launch
# ----------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app = create_app()
    app.run(host='0.0.0.0', port=port)


# TODO: Find how to use gettext on Jinja templates
# TODO: Generate Translation files for the project
# TODO: Upload code to both repos
