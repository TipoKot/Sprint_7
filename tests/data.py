BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

def get_test_order_payload(color):
    return {
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
