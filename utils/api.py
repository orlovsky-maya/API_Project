import json
from pathlib import Path
from utils.http_methods import HttpMethods


class GoogleMapsApi:
    base_url = 'https://rahulshettyacademy.com'
    key = '?key=qaclick123'
    d = Path(__file__).parent.absolute()

    def __init__(self, logger):
        self.http = HttpMethods(logger)

    def create_location(self):
        # Getting post url

        post_resource = '/maps/api/place/add/json'
        post_url = self.base_url + post_resource + self.key
        print(post_url)

        # Open json file

        with open(f'{self.d}/new_location_body.json', 'r', encoding='utf-8') as body_json:
            body_json = json.load(body_json)

        # POST request

        post_result = self.http.post(post_url, body_json)
        print(post_result.text)
        return post_result

    def get_location(self, place_id):
        # Getting get url

        get_resource = '/maps/api/place/get/json'
        get_url = self.base_url + get_resource + self.key + '&place_id=' + place_id
        print(get_url)

        # GET request

        get_result = self.http.get(get_url)
        print(get_result.text)
        return get_result

    def put_location(self, place_id):
        # Getting put url

        put_resource = '/maps/api/place/update/json'
        put_url = self.base_url + put_resource + self.key
        print(put_url)

        # Open json file

        with open(f'{self.d}/update_location_body.json', 'r', encoding='utf-8') as body_json:
            body_json = json.load(body_json)
            body_json['place_id'] = place_id

        # PUT Request

        put_result = self.http.put(put_url, body_json)
        print(put_result.text)
        return put_result

    def delete_location(self, place_id):
        # Getting delete url

        delete_resource = '/maps/api/place/delete/json'
        delete_url = self.base_url + delete_resource + self.key
        print(delete_url)

        # Open json file

        with open(f'{self.d}/update_location_body.json', 'r', encoding='utf-8') as body_json:
            body_json = json.load(body_json)
            body_json['place_id'] = place_id

        # DELETE Request

        delete_result = self.http.delete(delete_url, body_json)
        print(delete_result.text)
        return delete_result
