from utils.api import GoogleMapsApi


def test_create_new_place():
    print('Method POST')
    post_result = GoogleMapsApi.create_location()

    info_json = post_result.json()
    place_id = info_json.get('place_id')

    print('Method GET POST')
    get_result = GoogleMapsApi.get_location(place_id)

    print('Method PUT')
    put_result = GoogleMapsApi.put_location(place_id)

    print('Method GET PUT')
    get_result = GoogleMapsApi.get_location(place_id)

    print('Method DELETE')
    delete_result = GoogleMapsApi.delete_location(place_id)

    print('Method GET DELETE')
    get_result = GoogleMapsApi.get_location(place_id)

