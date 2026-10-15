from disk_api.client import DiskClient
import allure

@allure.feature("Авторизация")
@allure.title("Запрос без токена возвращает 401")
def test_request_without_token_returns_401():
    client = DiskClient()

    response = client.get_disk_info()

    assert response.status_code == 401

@allure.feature("Авторизация")
@allure.title("Запрос с неправильным токеном возвращает 401")
def test_request_with_invalid_token_returns_401():
    client = DiskClient("invalid-token-123")

    response = client.get_disk_info()

    assert response.status_code == 401