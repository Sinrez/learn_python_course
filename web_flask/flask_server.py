from flask import Flask
from weather import weather_by_city

app = Flask(__name__)

@app.route("/")
def hello():
    return "Привет!"

@app.route("/weather")
# http://127.0.0.1:5000/weather
def weather():
    weather = weather_by_city("Moscow,Russia")
    if weather:
        return f"Сейчас {weather['temp_C']},ощущается как {weather['FeelsLikeC']}"
    else:
        return "Прогноз сейчас недоступен"

if __name__=="__main__":
    app.run(debug=True)