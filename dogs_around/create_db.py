from webapp_dogs import create_app
from webapp_dogs.model import db

app = create_app()
with app.app_context():
        db.create_all()