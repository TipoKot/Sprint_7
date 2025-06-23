import requests
import allure
from data import BASE_URL

# Список заказов
# Проверь, что в тело ответа возвращается список заказов.
class TestOrderList:
    @allure.title("Test order list retrieval")
    def test_get_order_list(self):
        response = requests.get(f'{BASE_URL}/orders')
        assert response.status_code == 200, "Expected status code 200 for successful order list retrieval"
        data = response.json()
        assert isinstance(data["orders"], list), "Expected response to be a list"