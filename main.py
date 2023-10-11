from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_weather', methods=['POST'])
def get_weather():
    city_name = request.form['city']
    api_key = "412725df27378914a217850ce5b95f90"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        return render_template('weather_info.html', city=city_name, temperature=temperature, weather_description=weather_description)
    else:
        return render_template('incorrect_city.html')


if __name__ == '__main__':
    app.run(debug=True)
