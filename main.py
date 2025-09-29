from flask import Flask, render_template, request
from datetime import datetime
from src.configmanager import ConfigManager
from src.weatherservice import WeatherService

app = Flask(__name__)
config_manager = ConfigManager()
api_key = config_manager.get_value('API_KEY')
base_url = config_manager.get_value('BASE_URL')
weather_service = WeatherService(api_key, base_url)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_weather', methods=['POST'])
def get_weather():
    city_name = request.form['city']
    now = datetime.now()
    formatted_date_time = now.strftime("%A, %d %B %Y, %H:%M:%S")
    data = weather_service.get_weather(city_name)

    if data["cod"] == 200:
        temperature = round(data["main"]["temp"])
        weather_description = data["weather"][0]["description"].title()
        return render_template('weather_info.html', city=city_name, temperature=temperature,
                               weather_description=weather_description, date_time=formatted_date_time)
    else:
        return render_template('incorrect_city.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
