import os

from flask import Flask
from flask_wtf.csrf import CSRFProtect

from app.eg001_embedded_signing import eg001
from .views import core, ds

session_path = "/tmp/python_recipe_sessions"

quick_acg_app = Flask(__name__)
quick_acg_app.config.from_pyfile("../../config.py")

# See https://flask-wtf.readthedocs.io/en/stable/csrf.html
csrf = CSRFProtect(quick_acg_app)

# Register home page
quick_acg_app.register_blueprint(core)

# Register OAuth
quick_acg_app.register_blueprint(ds)
# Register examples
quick_acg_app.register_blueprint(eg001)

if "DYNO" in os.environ:  # On Heroku?
    import logging

    stream_handler = logging.StreamHandler()
    quick_acg_app.logger.addHandler(stream_handler)
    quick_acg_app.logger.setLevel(logging.INFO)
    quick_acg_app.logger.info("Recipe example startup")
    quick_acg_app.config.update(dict(PREFERRED_URL_SCHEME="https"))
