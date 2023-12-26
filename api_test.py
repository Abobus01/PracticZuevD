# api_test.py

import pytest
from faker import Faker
from calculator import Calculator

fake = Faker()

class TestCalculator:
    @pytest.fixture
    def calculator_instance(self):
        return Calculator()

    def test_addition(self, calculator_instance):
        num1 = fake.random_int()
        num2 = fake.random_int()
        result = calculator_instance.add(num1, num2)
        assert result == num1 + num2

    def test_subtraction(self, calculator_instance):
        num1 = fake.random_int()
        num2 = fake.random_int()
        result = calculator_instance.subtract(num1, num2)
        assert result == num1 - num2

    def test_multiplication(self, calculator_instance):
        num1 = fake.random_int()
        num2 = fake.random_int()
        result = calculator_instance.multiply(num1, num2)
        assert result == num1 * num2

    def test_division(self, calculator_instance):
        num1 = fake.random_int()
        num2 = fake.random_int()
        result = calculator_instance.divide(num1, num2)
        assert result == num1 / num2

    def test_zero_division(self, calculator_instance):
        with pytest.raises(ValueError):
            calculator_instance.divide(5, 0)