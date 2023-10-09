import json
from pathlib import Path
from utils.http_methods import HttpMethods


class GoogleMapsApi:
    base_url = 'https://rahulshettyacademy.com'
    key = '?key=qaclick123'
    d = Path(__file__).parent.absolute()

    @classmethod
    def create_location(cls):
        # Getting post url

        post_resource = '/maps/api/place/add/json'
        post_url = cls.base_url + post_resource + cls.key
        print(post_url)

        # Open json file

        with open(f'{cls.d}/new_location_body.json', 'r', encoding='utf-8') as body_json:
            body_json = json.load(body_json)

        # POST request

        post_result = HttpMethods.post(post_url, body_json)
        print(post_result.text)
        return post_result

    @classmethod
    def get_location(cls, place_id):
        # Getting get url

        get_resource = '/maps/api/place/get/json'
        get_url = cls.base_url + get_resource + cls.key + '&place_id=' + place_id
        print(get_url)

        # GET request

        get_result = HttpMethods.get(get_url)
        print(get_result.text)
        return get_result

    @classmethod
    def put_location(cls, place_id):
        # Getting put url

        put_resource = '/maps/api/place/update/json'
        put_url = cls.base_url + put_resource + cls.key
        print(put_url)

        # Open json file

        with open(f'{cls.d}/update_location_body.json', 'r', encoding='utf-8') as body_json:
            body_json = json.load(body_json)
            body_json['place_id'] = place_id

        # PUT Request

        put_result = HttpMethods.put(put_url, body_json)
        print(put_result.text)
        return put_result

    @classmethod
    def delete_location(cls, place_id):
        # Getting delete url

        delete_resource = '/maps/api/place/delete/json'
        delete_url = cls.base_url + delete_resource + cls.key
        print(delete_url)

        # Open json file

        with open(f'{cls.d}/update_location_body.json', 'r', encoding='utf-8') as body_json:
            body_json = json.load(body_json)
            body_json['place_id'] = place_id

        # DELETE Request

        delete_result = HttpMethods.delete(delete_url, body_json)
        print(delete_result.text)
        return delete_result

