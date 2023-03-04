from flask import Flask, render_template
from webapp.weather import weather_by_city
from webapp.bs_ex import get_python_news
from webapp.model import db, News
from webapp.forms import LoginForm


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # from . import model
    # with app.app_context():
    #     db.create_all()

    @app.route('/login')
    def login():
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    @app.route("/")
    def weather():
        title = 'Новостной сайт'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page_title=title, weather=weather, news_list=news)
    
    return app

