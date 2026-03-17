import math_utils

if __name__ == "__main__":
    n = int(input("Введите число: "))
    print(f"Квадрат: {math_utils.square(n)}")
    print(f"Куб: {math_utils.cube(n)}")
    print(f"Чётное: {math_utils.is_even(n)}")
