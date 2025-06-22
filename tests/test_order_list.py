import requests

# Список заказов
# Проверь, что в тело ответа возвращается список заказов.

def test_get_order_list():
    response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
    print(response.json())  # Выводим ответ для отладки
    assert response.status_code == 200, "Expected status code 200 for successful order list retrieval"
    data = response.json()
    assert isinstance(data["orders"], list), "Expected response to be a list"