from utils.api import GoogleMapsApi
from utils.checking import Checking


def test_crud_place():
    print('Method POST')
    post_result = GoogleMapsApi.create_location()
    Checking.checking_status_code(post_result, 200)
    Checking.check_json_fields(post_result, ['status', 'place_id', 'scope', 'reference', 'id'])
    Checking.check_json_value(post_result, "status", "OK")

    info_json = post_result.json()
    place_id = info_json.get('place_id')

    print('Method GET POST')
    get_result = GoogleMapsApi.get_location(place_id)
    Checking.checking_status_code(get_result, 200)
    Checking.check_json_fields(get_result, ['location', 'accuracy', 'name', 'phone_number', 'address',
                                            'types', 'website', 'language'])
    Checking.check_json_value(get_result, "address", "29, side layout, cohen 09")

    print('Method PUT')
    put_result = GoogleMapsApi.put_location(place_id)
    Checking.checking_status_code(put_result, 200)
    Checking.check_json_fields(put_result, ['msg'])
    Checking.check_json_value(put_result, "msg", "Address successfully updated")

    print('Method GET PUT')
    get_result = GoogleMapsApi.get_location(place_id)
    Checking.checking_status_code(get_result, 200)
    Checking.check_json_fields(get_result, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                            'website', 'language'])
    Checking.check_json_value(get_result, "address", "100 Lenina street, RU")

    print('Method DELETE EXIST')
    delete_result = GoogleMapsApi.delete_location(place_id)
    Checking.checking_status_code(delete_result, 200)
    Checking.check_json_fields(delete_result, ['status'])
    Checking.check_json_value(delete_result, "status", "OK")

    print('Method GET DELETE')
    get_result = GoogleMapsApi.get_location(place_id)
    Checking.checking_status_code(get_result, 404)
    Checking.check_json_fields(get_result, ['msg'])
    Checking.check_json_value(get_result, "msg", "Get operation failed, looks like place_id "
                                                 " doesn't exists")

    print('Method DELETE NOT EXIST')
    delete_result = GoogleMapsApi.delete_location(place_id)
    Checking.checking_status_code(delete_result, 404)
    Checking.check_json_fields(delete_result, ['msg'])
    Checking.check_json_value(delete_result, "msg", "Delete operation failed, "
                                                    "looks like the data doesn't exists")

    print('Testing "create, get, update, delete" location is pass')
