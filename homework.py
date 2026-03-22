from typing import Any, Callable, Generator
from operator import add, mul, sub, truediv


# 1. Используя filter() и lambda, отфильтруйте из списка [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] только нечетные числа.

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers: list[int] = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # Вывод: [1, 3, 5, 7, 9]    

# 2. Напишите функцию apply_operations(numbers, *operations), 
# которая принимает список чисел и произвольное количество lambda-функций, 
# последовательно применяя каждую ко всему списку.

def apply_operations(numbers: list[int], *operations: Callable[[int], int]) -> list[int]:
    for operation in operations:
        numbers = list(map(operation, numbers))
    return numbers  


# 3. Напишите генератор chunked(lst, size), который разбивает список на куски заданного размера и поочередно их выдает.
#  Например, chunked([1,2,3,4,5], 2) → [1,2], [3,4], [5].

def chunked(lst: list[int], size: int) -> Generator:
    for i in range(0, len(lst), size):
        yield lst[i:i + size]   

# 4. Напишите генератор prime_numbers(), который бесконечно генерирует простые числа. Выведите первые 20.
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 5. Напишите функцию safe_convert(value, type_func), 
# которая пытается преобразовать value с помощью переданной функции (например, int, float). 
# При ошибке возвращает None.
def safe_convert(value: Any, type_func: Callable) -> Any | None:
    try:
        return type_func(value)
    except (ValueError, TypeError):
        return None

# 6. Создайте собственный класс исключения NegativeNumberError. Напишите функцию sqrt_safe(n), 
# которая считает квадратный корень из числа, но при отрицательном n выбрасывает NegativeNumberError с понятным сообщением.
class NegativeNumberError(Exception):
    pass

def sqrt_safe(n: float) -> float:
    if n < 0:
        raise NegativeNumberError("Нельзя вычислить квадратный корень из отрицательного числа")
    return n ** 0.5

# 7. Напишите функцию-калькулятор calculator(a, b, op), где op — строка ("+", "-", "*", "/"). 
# Обработайте все возможные исключения: деление на ноль, неизвестная операция, некорректные типы аргументов.

def calculator(a: float, b: float, op: str) -> float | str:
    operations: dict[str, Callable] = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": truediv,
    }

    func = operations.get(op)
    if func is None:
        return "Ошибка: неизвестная операция"

    try:
        return func(a, b)
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"
    except TypeError:
        return "Ошибка: некорректные типы аргументов"
    