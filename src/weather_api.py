import requests


class WeatherAPI:
    """
    Handles fetching weather information using an external API.
    """

    def __init__(self, api_key, base_url):
        """
        Initializes the WeatherService with the necessary API credentials.

        :param api_key: Your API key for the weather service.
        :param base_url: The base URL for the weather API endpoints.
        """
        self.api_key = api_key
        self.base_url = base_url

    def get_weather(self, city_name: str) -> dict:
        """
        Fetches weather information for a given city.

        :param city_name: The name of the city(en) to fetch weather data for.
        :return: A dictionary containing the weather data.
        """
        complete_url = f"{self.base_url}q={city_name}&appid={self.api_key}&units=metric"
        response = requests.get(complete_url)
        return response.json()
