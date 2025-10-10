from flask import Flask, render_template, request
from datetime import datetime
from src.environment_manager import EnvironmentManager
from src.weather_api import WeatherAPI, ResponseStatus

app = Flask(__name__)
env_manager = EnvironmentManager()
api_key = env_manager.get_env_value('API_KEY')
base_url = env_manager.get_env_value('BASE_URL')
weather_api = WeatherAPI(api_key, base_url)

@app.context_processor
def utility_processor():
    return dict(round=round)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/get_weather', methods=['POST'])
def get_weather():
    city_name = request.form['city']
    date_time_now = datetime.now().strftime("%A, %d %B %Y, %H:%M:%S")
    data = weather_api.get_weather(city_name)
    if data["cod"] == ResponseStatus.OK:
        return render_template('weather_info.html', data=data, date_time_now=date_time_now)
    else:
        return render_template('incorrect_city.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
