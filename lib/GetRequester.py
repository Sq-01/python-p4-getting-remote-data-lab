import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'

        response = requests.get(url)
        return response.content


    def load_json(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raises an HTTPError if the response was an HTTP error
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error during requests to {self.url} : {str(e)}")
            return None