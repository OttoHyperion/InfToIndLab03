from src import lib
import pytest

# Позитивный тест с корректными данными. Возвращает  последовательность Фибоначчи
def test_positive_fibonacci():
    assert lib.fibonacci(5).tolist() == [0, 1, 1, 2, 3]

