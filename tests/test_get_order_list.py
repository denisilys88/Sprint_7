import allure
from client_requests import ClientRequests as Client


class TestGetOrderList:

    @allure.title('Проверка получения списка заказов по курьеру')
    @allure.description('Создаем курьера, логиним курьера, создаем заказ, получаем id заказа, принимаем заказ курьером,'
                        'получаем список заказов, проверяем, что в ответе получаем статус 200 и содержится список заказов ')
    def test_get_order_list(self, new_courier, new_order):
        payload = {'login': new_courier['login'], 'password': new_courier['password']}
        client = Client()
        response_login = client.post_login(payload)
        courier_id = response_login.json()['id']
        client.put_accept_order(courier_id, new_order['id'])
        response_get_order_list = client.get_order_list(courier_id)
        order = response_get_order_list.json()['orders']
        assert isinstance(order, list)
        assert response_get_order_list.status_code == 200