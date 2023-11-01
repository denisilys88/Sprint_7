import random
import allure
from client_requests import ClientRequests as Client


class TestDeleteCourier:

    @allure.title('Проверка успешного удаления сущности курьера')
    @allure.description('Создаем сущность курьера, логинимся с этими данными, получаем id курьера, удаляем курьера'
                        'проверяем, что в ответе получаем статус 200 и сообщение - ok: true'
                        'пробуем залогиниться с удаленным курьером - проверяем, что в ответе получаем статус 404 '
                        'и сообщение - Учетная запись не найдена')
    def test_delete_courier_success(self, new_courier):
        payload = {'login': new_courier['login'], 'password': new_courier['password']}
        client = Client()
        response_login = client.post_login(payload)
        courier_id = response_login.json()['id']
        response_delete = client.delete_courier(courier_id)
        response_login = client.post_login(payload)
        assert response_delete.status_code == 200
        assert response_delete.json() == {'ok': True}
        assert response_login.status_code == 404
        assert response_login.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Проверка удаления курьера без айди')
    @allure.description('Удаляем без айди, проверяем, что в ответе получим статус 404 и сообщение - Not Found')
    def test_delete_courier_without_id(self):
        client = Client()
        response_delete = client.delete_courier('')
        assert response_delete.status_code == 404
        assert response_delete.json()['message'] == 'Not Found.'

    @allure.title('Проверка удаления несуществующего курьера')
    @allure.description('Удаляем курьера с несуществующим айди, проверяем, что в ответе получим статус 404 и '
                        'сообщение - Курьера с таким id нет.')
    def test_delete_non_existed_courier(self):
        client = Client()
        non_existed_courier_id = random.randint(0, 100000000)
        response_delete = client.delete_courier(non_existed_courier_id)
        assert response_delete.status_code == 404
        assert response_delete.json()['message'] == 'Курьера с таким id нет.'
