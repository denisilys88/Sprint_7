import allure
import pytest
from data import Data
from client_requests import ClientRequests as Client


class TestCreateCourier:


    @allure.title('Проверка создания сущности курьера')
    @allure.description('Создаем сущность курьера, проверяем, что в ответе возвращается ok: True '
                        'затем логинимся с теми же данными, проверяем, что в ответе получаем статус 200 и id курьера')
    def test_create_courier(self, new_courier):
        payload = {'login': new_courier['login'], 'password': new_courier['password']}
        client = Client()
        response_login = client.post_login(payload)
        assert new_courier['json'] == {'ok': True}
        assert response_login.status_code == 200
        assert 'id' in response_login.json()

    @allure.title('Проверка невозможности создания двух одинаковых сущностей курьера')
    @allure.description('Создаем сущность курьера, затем еще раз пытаемся создать сущность с теми же данными, '
                        'проверяем, что в ответе получаем статус 409 и сообщение Этот логин уже используется. Попробуйте '
                        'другой.')
    def test_create_two_same_courier(self, new_courier):
        payload = {'login': new_courier['login'], 'password': new_courier['password'], 'firstName': new_courier['firstName']}
        client = Client()
        response_create = client.post_create(payload)
        assert response_create.status_code == 409
        assert response_create.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Проверка создания сущности курьера без одного из обязательных полей')
    @allure.description('Создаем сущность курьера без логина, без пароля'
                        'проверяем, что в ответе получаем статус 400 и сообщение Недостаточно данных для создания учетной записи')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_create_courier_without_mandatory_fields(self, field):
        payload = {'login': Data.NAME, 'password': Data.PASSWORD, 'firstName': Data.FIRSTNAME}
        payload.pop(field)
        client = Client()
        response_create = client.post_create(payload)
        assert response_create.status_code == 400
        assert response_create.json()['message'] == 'Недостаточно данных для создания учетной записи'
