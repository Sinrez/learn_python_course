from flask import Flask
from weather import weather_by_city
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Привет!"

@app.route("/weather")
# http://127.0.0.1:5000/weather
def weather():
    title = 'Новостной сайт'
    weather = weather_by_city("Moscow,Russia")
    return render_template('index.html', page_title=title, weather=weather)

if __name__=="__main__":
    app.run(debug=True)