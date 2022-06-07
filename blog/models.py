from flask_sqlalchemy import SQLAlchemy

from blog.settings import BIND_KEY

db = SQLAlchemy()


class User(db.Model):
    __bind_key__ = BIND_KEY
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    image_file = db.Column(db.String(), nullable=False, default='img/mem.png')
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'User({self.username}'
