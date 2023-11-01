import allure
import pytest
from helpers import Helpers
from client_requests import ClientRequests as Client


class TestLoginCourier:

    @allure.title('Проверка логина курьера без одного из обязательных полей')
    @allure.description('Логиним курьера без логина, без пароля '
                        'проверяем, что в ответе получаем статус 400 и сообщение Недостаточно данных для входа')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_login_courier_without_mandatory_fields(self, new_courier, field):
        payload = {'login': new_courier['login'], 'password': new_courier['password']}
        payload.pop(field)
        client = Client()
        response_create = client.post_login(payload)
        assert response_create.status_code == 400
        assert response_create.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Проверка логина курьера с неверным паролем')
    @allure.description('Логиним курьера с существующим логином с неправильным паролем'
                        'проверяем, что в ответе получаем статус 404 и сообщение Учетная запись не найдена')
    def test_login_courier_with_wrong_password(self, new_courier):
        payload = {'login': new_courier['login'], 'password': '12345'}
        client = Client()
        response_create = client.post_login(payload)
        assert response_create.status_code == 404
        assert response_create.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Проверка логина курьера с несуществующим логином')
    @allure.description('Логиним курьера с несуществующим логином с существующим паролем'
                        'проверяем, что в ответе получаем статус 404 и сообщение Учетная запись не найдена')
    def test_login_courier_with_non_existed_login(self, new_courier):
        payload = {'login': Helpers.generate_random_string(10), 'password': new_courier['password']}
        client = Client()
        response_create = client.post_login(payload)
        assert response_create.status_code == 404
        assert response_create.json()['message'] == 'Учетная запись не найдена'
