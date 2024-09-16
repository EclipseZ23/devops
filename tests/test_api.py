import requests
from calculator_client.client import Client
from calculator_client.api.actions import calculate
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.models import ResultResponse


class TestCalculatorAPI():
    def test_calculator_add(self):
        url = "http://127.0.0.1:5000/calculate"

        payload = {
            "operation": "add",
            "operand1": 4,
            "operand2": 7
        }

        response = requests.post(url, json=payload)
        
    def test_generated_code(self):
        client = Client("http://127.0.0.1:5000")
        response = calculate.sync(client = client, body = Calculation(Opertions.ADD, operand1=1, operand2=1))
        assert isinstance(response, ResultResponse)
        assert response.result == 2
