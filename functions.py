# Напиши код который выведет таблицу умножения до 10 на N (введенное с клавиатуры) в таком формате
#   3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27

def multiplication_table(n: int) -> None:
    for i in range(1, 10):
        end = "\n" if i == 9 else " | "
        print(n * i, end=end)


n = int(input("Введите число N: "))
multiplication_table(n)


# Попроси пользователя ввести имя и возраст. Выведи фразу: «Через 10 лет тебе будет <X> лет, <ИМЯ>!»

def user_info(name: str, year: int) -> None:
    print(f'Через 10 лет тебе будет {year + 10} лет, {name}!')

name = str(input('Введите Ваше имя: '))
year = int(input('Введите Ваш возраст: '))
user_info(name, year)


# Даны два списка цен в долларах и курс валюты. Используй map чтобы перевести все цены в рубли. Затем используй zip чтобы создать словарь {товар: цена_в_рублях}:

items = ['хлеб', 'молоко', 'кофе']
prices_usd = [1.5, 2.0, 8.0]
rate = 3.2

def prices(items: list[str], prices_usd: list[float], rate: float) -> dict[str, float]:
    def to_rub(p: float) -> float:
        return p * rate
    
    new_prices = map(to_rub, prices_usd)
    item_prices = dict(zip(items, new_prices))
    return item_prices

print(prices(items, prices_usd, rate))


# Напиши функцию fizzbuzz(n) которая принимает число и возвращает строку:
# 'Fizz' если делится на 3, 'Buzz' если делится на 5, 'FizzBuzz' если делится на оба,
# иначе само число в виде строки. Вызови её для чисел от 1 до 20 через map.

def fizzbuzz(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

print(list(map(fizzbuzz, range(1, 21))))


# Напиши функцию *args с именем my_stats которая принимает любое количество чисел
# и возвращает сразу три значения — минимум, максимум и среднее.

def my_stats(*args: float) -> tuple[float, float, float]:
    return min(args), max(args), sum(args) / len(args)

print(my_stats(3, 7, 1, 9, 4))


# Напиши функцию build_profile(**kwargs) которая принимает любые именованные аргументы
# и возвращает словарь с этими данными плюс автоматически добавляет ключ 'registered': True.

def build_profile(**kwargs) -> dict:
    """Принимает любые именованные аргументы и возвращает словарь профиля.
    
    Автоматически добавляет ключ 'registered': True к переданным данным.
    """
    kwargs['registered'] = True
    return kwargs

print(build_profile(name='Елена', age=25, city='Киев'))

