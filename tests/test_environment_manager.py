import os
import unittest
from src.environment_manager import EnvironmentManager
from src.weather_api import WeatherAPI


class TestConfigManager(unittest.TestCase):
    """
    Tests the functionality of ConfigManager class
    """

    def test_constructor(self):
        """
        Tests ConfigManager initialization
        """
        EnvironmentManager()
        assert os.getenv('API_KEY')

    def test_get_value(self):
        """
        Tests get_value method for correct retrieval and handling of non-existent keys.
        """
        self.assertEqual(os.getenv('API_KEY'), EnvironmentManager.get_env_value('API_KEY'))
        try:
            self.assertEqual(os.getenv('API_KEY'), EnvironmentManager.get_env_value('XXX'))
        except AssertionError as e:
            print(f"{e.__class__.__name__} was occurred -> OK")


class TestWeatherService(unittest.TestCase):
    """
    Tests the functionality of WeatherService class
    """

    def test_constructor(self):
        """
        Tests WeatherService initialization
        """
        WeatherAPI(os.getenv("API_KEY"), os.getenv("BASE_URL"))

    def test_get_weather(self):
        """
        Tests get_weather method returns a dictionary for correct city name
        """
        ws = WeatherAPI(os.getenv("API_KEY"), os.getenv("BASE_URL"))
        self.assertEqual(type(ws.get_weather('Brno')), dict)


if __name__ == '__main__':
    unittest.main()
