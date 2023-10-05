from requests import Response
from utils.api import GoogleMapsApi


def test_create_new_place():
    print('Method POST')
    post_result: Response = GoogleMapsApi.create_location()
