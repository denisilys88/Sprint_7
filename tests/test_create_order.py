import allure
import pytest
from helpers import Helpers
from client_requests import ClientRequests as Client


class TestCreateOrder:

    @allure.title('Проверка успешного создания заказа')
    @allure.description('Создаем заказ с полным набором данных, меняя значение поля color'
                        'ожидаем, что в ответе статус 201 и содержится трек номер заказа')
    @pytest.mark.parametrize('color', ['black', 'grey', 'both', 'none'])
    def test_login_courier_without_mandatory_fields(self, color):
        payload = Helpers.get_payload_for_order(color)
        client = Client()
        response_order = client.post_order(payload)
        assert response_order.status_code == 201
        assert 'track' in response_order.json()
