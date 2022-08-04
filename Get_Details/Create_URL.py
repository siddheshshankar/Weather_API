import os


class CreateURL:

    def __init__(self, location):
        self.location = location

    def get_api_key(self):
        """
        Reads API key from a file. It is advisable to read key values from a file instead of hard coding it.
        :return: API key value
        """
        with open(os.path.join(os.getcwd(), 'API_Key')) as f:
            return f.readline()

    def get_web_url(self):
        """
        Creates URL link for a particular location
        :return: web URL
        """
        return f"http://api.openweathermap.org/data/2.5/weather?q={self.location}&appid={self.get_api_key()}"
