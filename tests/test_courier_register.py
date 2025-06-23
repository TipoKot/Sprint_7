import requests
import random
import string
import allure
from register import register_new_courier_and_return_login_password
from data import BASE_URL

class TestCourierRegistration:
    @allure.title("Test courier registration")
    def test_create_courier(self):
        new_courier = register_new_courier_and_return_login_password()
        assert new_courier.__len__() == 3, "Courier registration failed, expected 3 items in the list"

    @allure.title("Test duplicate courier registration")
    def test_create_duplicate_courier(self):
        new_courier = register_new_courier_and_return_login_password()

        payload = {
        "login": new_courier[0],
        "password": new_courier[1],
        "firstName": new_courier[2]
        }

        response = requests.post(f'{BASE_URL}/courier', data=payload)
        assert response.status_code == 409, "Expected status code 409 for duplicate courier creation"

    @allure.title("Test create courier without required fields")
    def test_create_courier_without_required_fields(self):
        payload = {
            "login": "",
            "password": "",
            "firstName": ""
        }

        response = requests.post(f'{BASE_URL}/courier', data=payload)
        assert response.status_code == 400, "Expected status code 400 for missing required fields"

    @allure.title("Test create courier with random data")
    def test_create_courier_with_random_data(self):
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
        response = requests.post(f'{BASE_URL}/courier', data=payload)
        assert response.status_code == 201, "Expected status code 201 for successful courier creation"
        assert response.json() == {"ok": True}, "Expected response to be {'ok': True} for successful courier creation"

    @allure.title("Test register courier with missing one field")
    def test_create_courier_missing_one_field(self):
        payload = {
            "login": "test_courier",
            "password": "",  # Missing password
            "firstName": "Test"
        }

        response = requests.post(f'{BASE_URL}/courier', data=payload)
        assert response.status_code == 400, "Expected status code 400 for missing required fields"
