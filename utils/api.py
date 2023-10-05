import json
from utils.http_methods import HttpMethods


class GoogleMapsApi:
    base_url = 'https://rahulshettyacademy.com'
    key = '?key=qaclick123'

    @classmethod
    def create_location(cls):
        # Getting post url

        post_resource = '/maps/api/place/add/json'
        post_url = cls.base_url + post_resource + cls.key
        print(post_url)

        # Open json file

        with open('./tests/new_location_body.json', 'r', encoding='utf-8') as body_json:
            body_json = json.load(body_json)

        # POST request

        post_result = HttpMethods.post(post_url, body_json)
        print(post_result.text)
        return post_result
