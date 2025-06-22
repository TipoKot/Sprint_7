import requests
import random
import string
from register import register_new_courier_and_return_login_password

# Проверяем, что курьера можно создать
def test_create_courier():
    new_courier = register_new_courier_and_return_login_password()

    assert new_courier.__len__() == 3, "Courier registration failed, expected 3 items in the list"

# Проверяем, что нельзя создать двух одинаковых курьеров
def test_create_duplicate_courier():
    new_courier = register_new_courier_and_return_login_password()
    
    payload = {
        "login": new_courier[0],
        "password": new_courier[1],
        "firstName": new_courier[2]
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    assert response.status_code == 409, "Expected status code 409 for duplicate courier creation"

# Проверяем, что курьера нельзя создать без обязательных полей
def test_create_courier_without_required_fields():
    payload = {
        "login": "",
        "password": "",
        "firstName": ""
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    assert response.status_code == 400, "Expected status code 400 for missing required fields"

# Проверяем, что запрос возвращает правильный код ответа
def test_create_courier_response_code():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    assert response.status_code == 201, "Expected status code 201 for successful courier creation"
    assert response.json() == {"ok": True}, "Expected response to be {'ok': True} for successful courier creation"

def test_create_courier_missing_one_fields():
    payload = {
        "login": "test_courier",
        "password": "",  # Missing password
        "firstName": "Test"
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    assert response.status_code == 400, "Expected status code 400 for missing required fields"
