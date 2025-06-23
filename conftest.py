import pytest
from register import register_new_courier_and_return_login_password, delete_courier_by_login_and_password   

@pytest.fixture
def valid_courier():
    login, password, first_name = register_new_courier_and_return_login_password()

    yield {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # teardown — удаление курьера
    delete_courier_by_login_and_password(login, password)
