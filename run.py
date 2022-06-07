from blog import app_ctx
from blog.models import db

from blog.routes import IndexView

if __name__ == '__main__':
    with app_ctx.app_context():
        db.create_all()
        app_ctx.run(debug=True)