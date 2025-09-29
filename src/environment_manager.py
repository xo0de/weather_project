from dotenv import load_dotenv
import os


class EnvironmentManager:
    """
    Loads and retrieves environment variables from a .env file.
    """

    def __init__(self):
        """
        Loads environment variables.
        """
        load_dotenv()

    @staticmethod
    def get_env_value(key: str) -> str:
        """
        Returns the value of an environment variable by its key.

        :param key: The environment variable name.
        :return: The value of the environment variable, or None if not found.
        """
        return os.getenv(key)
