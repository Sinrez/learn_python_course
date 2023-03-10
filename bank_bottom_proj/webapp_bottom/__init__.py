# ./run.sh
# source env_bottom/bin/activate
# export FLASK_APP=webapp_bottom && flask db init

from flask import Flask, render_template, flash, redirect, url_for
from webapp_bottom.model  import db, Feedback
from flask_migrate import Migrate
import datetime 


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
 
    @app.route("/")
    def index():
        title = 'Дно банки'
        delta = datetime.timedelta(days=7)
        now_day = datetime.date.today()
        delta_days = now_day - delta
        qr = db.session.query(Feedback.bank_name,db.func.count(Feedback.url_page)).filter(Feedback.response_date > delta_days).group_by(Feedback.bank_name).having(db.func.count(Feedback.url_page) > 10).order_by(db.func.count(Feedback.url_page).desc()).all()
        return render_template('index.html', page_title=title, banks_list= qr)
    
    @app.route("/feedback")
    def get_feedback():
        title = 'Дно банки'
        news = Feedback.query.order_by(Feedback.response_date.desc()).all()
        return render_template('feedback.html', page_title=title, news_list=news)
    
    return app