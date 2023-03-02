from flask import Flask, render_template
from weather import weather_by_city
from bs_ex import get_python_news


app = Flask(__name__)

@app.route("/")
def hello():
    return "Привет!"

@app.route("/weather")
# http://127.0.0.1:5000/weather
def weather():
    title = 'Новостной сайт'
    weather = weather_by_city("Moscow,Russia")
    news = get_python_news()
    return render_template('index.html', page_title=title, weather=weather, news_list=news)

if __name__=="__main__":
    app.run(debug=True)