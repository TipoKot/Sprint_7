import pytest
import requests
from data import BASE_URL, get_test_order_payload

# Проверь, что, когда создаёшь заказ:
    # можно указать один из цветов — BLACK или GREY;
    # можно указать оба цвета;
    # можно совсем не указывать цвет;
    # тело ответа содержит track.
# Чтобы протестировать создание заказа, нужно использовать параметризацию.
class TestCreateOrder:
    @pytest.mark.parametrize("color", [
        "BLACK",
        "GREY",
        "BLACK, GREY",
        ""
    ])
    def test_create_order(self, color):
        payload = get_test_order_payload(color)

        response = requests.post(f'{BASE_URL}/orders', json=payload)

        assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
        assert "track" in response.json(), "Expected response to contain 'track'"