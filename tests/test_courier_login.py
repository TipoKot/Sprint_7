import requests
from register import register_new_courier_and_return_login_password

# Проверь:
    # если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;
    # успешный запрос возвращает id.

def test_courier_login():
    new_courier = register_new_courier_and_return_login_password()
    
    payload = {
        "login": new_courier[0],
        "password": new_courier[1]
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
    assert response.status_code == 200, "Expected status code 200 for successful login"
    assert "id" in response.json(), "Expected response to contain 'id' for successful login"

def test_courier_login_with_missin_credentials():
    new_courier = register_new_courier_and_return_login_password()
    payload = {
        "login": new_courier[0],
        "password": ""
    }
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
    assert response.status_code == 400, "Expected status code 400 for missing credentials"

def test_courier_login_with_invalid_credentials():
    payload = {
        "login": "invalid_login",
        "password": "invalid_password"
    }
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
    assert response.status_code == 404, "Expected status code 404 for invalid credentials"