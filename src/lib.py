import numpy as np

# Функция определения чисел Фибоначчи
# Принимает n чисел
# Возвращает список последовательности Фибоначчи = n
# Пример: n = 7 => [0 1 1 2 3 5 8]
def fibonacci(n):
    if n <= 0:
        raise ValueError("need n > 0")
    fib_arr = np.zeros(n)
    fib_arr[1] = 1
    for i in range(2, n):
        fib_arr[i] = fib_arr[i - 2] + fib_arr[i - 1]
    return fib_arr



