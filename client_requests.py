import allure
import requests


class ClientRequests:

    def __init__(self):
        self.host = 'http://qa-scooter.praktikum-services.ru'

    @allure.step('вызываем нужный метод requests по переданным параметрам')
    def make_request(self, path, type, payload=None):
        response = ''
        url = f'{self.host}{path}'
        if type == 'post':
            response = requests.post(url, data=payload)
        elif type == 'get':
            response = requests.get(url, data=payload)
        elif type == 'delete':
            response = requests.delete(url)
        elif type == 'put':
            response = requests.put(url, data=payload)
        elif type == 'patch':
            response = requests.patch(url, data=payload)
        return response

    @allure.step('вызываем метод make_request для ручки создания курьера')
    def post_create(self, payload):
        path = f"/api/v1/courier"
        return self.make_request(path, 'post', payload)

    @allure.step('вызываем метод make_request для ручки логина курьера')
    def post_login(self, payload):
        path = f"/api/v1/courier/login"
        return self.make_request(path, 'post', payload)

    @allure.step('вызываем метод make_request для ручки создания заказа')
    def post_order(self, payload):
        path = f"/api/v1/orders"
        return self.make_request(path, 'post', payload)

    @allure.step('вызываем метод make_request для ручки принятия заказа')
    def put_accept_order(self, courier, order):
        path = f"/api/v1/orders/accept/{order}?courierId={courier}"
        return self.make_request(path, 'put')

    @allure.step('вызываем метод make_request для ручки получения заказа по его номеру')
    def get_order_id_by_track(self, track):
        path = f"/api/v1/orders/track?t={track}"
        return self.make_request(path, 'get')

    @allure.step('вызываем метод make_request для ручки получения списка заказов')
    def get_order_list(self, courier):
        path = f"/api/v1/orders?courierId={courier}"
        return self.make_request(path, 'get')

    @allure.step('вызываем метод make_request для ручки удаления курьера')
    def delete_courier(self, courier=''):
        path = f"/api/v1/courier/{courier}"
        return self.make_request(path, 'delete')
