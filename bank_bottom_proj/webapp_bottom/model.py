from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Feedback(db.Model):
        id_url = db.Column(db.String,unique=True, primary_key=True)
        url_page = db.Column(db.String, unique=True, nullable=False)
        bank_name = db.Column(db.String, nullable=False)
        category = db.Column(db.String, nullable=False)
        short_feedback = db.Column(db.String, nullable=False)
        response_date = db.Column(db.DateTime, nullable=False)
        response_city = db.Column(db.String, nullable=False)
        response_full = db.Column(db.Text, nullable=True)
    
        def __repr__(self):
            return f' Отзыв: {self.bank_name}, {self.category}, {self.short_feedback}, {self.url_page}'

class User(db.Model):
        id_user = db.Column(db.String,unique=True, primary_key=True, nullable=False)
        first_name = db.Column(db.String, nullable=True)
        last_name = db.Column(db.String, nullable=True)
        user_name = db.Column(db.String, nullable=True)
        chat_id = db.Column(db.String,unique=True, nullable=False)
        subscribed = db.Column(db.Boolean, default=False)

      