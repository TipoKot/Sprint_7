import requests
import allure
from register import register_new_courier_and_return_login_password
from data import BASE_URL
from conftest import valid_courier

# Проверь:
    # если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;
    # успешный запрос возвращает id.

class TestCourierLogin:
    @allure.title("Test courier login functionality")
    def test_courier_login(self, valid_courier):
        courier = valid_courier

        response = requests.post(f'{BASE_URL}/courier/login', data=courier)
        assert response.status_code == 200, "Expected status code 200 for successful login"
        assert "id" in response.json(), "Expected response to contain 'id' for successful login"

    @allure.title("Test courier login with missing credentials")
    def test_courier_login_with_missing_credentials(self):
        new_courier = register_new_courier_and_return_login_password()
        payload = {
            "login": new_courier[0],
            "password": ""
        }
        response = requests.post(f'{BASE_URL}/courier/login', data=payload)
        assert response.status_code == 400, "Expected status code 400 for missing credentials"
        assert "Недостаточно данных для входа" in response.text, "Expected error message for missing credentials"

    @allure.title("Test courier login with invalid credentials")
    def test_courier_login_with_invalid_credentials(self):
        payload = {
            "login": "invalid_login",
            "password": "invalid_password"
        }
        response = requests.post(f'{BASE_URL}/courier/login', data=payload)
        assert response.status_code == 404, "Expected status code 404 for invalid credentials"
        assert "Учетная запись не найдена" in response.text, "Expected error message for invalid credentials"