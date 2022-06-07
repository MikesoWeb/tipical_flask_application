from flask import Flask

from blog.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    db.init_app(app)
    return app


app_ctx = create_app()
