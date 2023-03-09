# from webapp import db, create_app
# db.create_all(app=create_app())

from webapp_bottom import create_app
from webapp_bottom.model import db

app = create_app()
with app.app_context():
        db.create_all()