from flask import Flask, render_template
from webapp.weather import weather_by_city
from webapp.bs_ex import get_python_news

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route("/")
    def weather():
        title = 'Новостной сайт'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news = get_python_news()
        return render_template('index.html', page_title=title, weather=weather, news_list=news)
    return app
