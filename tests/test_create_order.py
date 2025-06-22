import pytest
import requests

# Проверь, что, когда создаёшь заказ:
    # можно указать один из цветов — BLACK или GREY;
    # можно указать оба цвета;
    # можно совсем не указывать цвет;
    # тело ответа содержит track.
# Чтобы протестировать создание заказа, нужно использовать параметризацию.

@pytest.mark.parametrize("color", [
    "BLACK",
    "GREY",
    "BLACK, GREY",
    ""
])
def test_create_order(color):
    payload = {
        "firstName": "Test",
        "lastName": "User",
        "address": "Test Address",
        "metroStation": 1,
        "phone": "+79999999999",
        "rentTime": 5,
        "deliveryDate": "2023-10-01",
        "comment": "Test Comment",
        "color": color.split(", ") if color else []
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=payload)
    
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
    assert "track" in response.json(), "Expected response to contain 'track'"