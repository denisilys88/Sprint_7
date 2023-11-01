import pytest
from helpers import Helpers
from client_requests import ClientRequests as Client


@pytest.fixture()
def new_courier():

    login = Helpers.generate_random_string(10)
    password = Helpers.generate_random_string(10)
    first_name = Helpers.generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    info_response = {}

    client = Client()
    response_post = client.post_create(payload)

    info_response['login'] = login
    info_response['password'] = password
    info_response['firstName'] = first_name
    info_response['status_code'] = response_post.status_code
    info_response['json'] = response_post.json()

    if response_post.status_code == 201:
        yield info_response
    else:
        raise Exception('не получен успешный статус 201 для создания сущности курьера')


@pytest.fixture()
def new_order():
    client = Client()
    order_info = {}
    payload_for_order = Helpers.get_payload_for_order('')
    response_order = client.post_order(payload_for_order)
    order_track = response_order.json()['track']
    response_get_order_id = client.get_order_id_by_track(order_track)
    if response_get_order_id.status_code == 200:
        order_info['id'] = response_get_order_id.json()['order']['id']
        yield order_info
    else:
        raise Exception('не получен успешный статус 200 для получения id заказа по трек-номеру')
