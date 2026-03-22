import os
from datetime import datetime


# 1. Напиши функцию copy_file(source: str, destination: str) -> bool,
#  которая читает содержимое файла source и записывает его в destination. Возвращает True если успешно. 
# Проверь что файл-копия создался.

def copy_file(source: str, destination: str) -> bool:
    with open(source, 'r') as f:
        content = f.read()
    with open(destination, 'w') as f:
        f.write(content)
    return os.path.isfile(destination) and os.path.getsize(destination) == os.path.getsize(source)

copy_file('file_1.py', 'file_1_copy.py')


# 2. Напиши код который читает файл и добавляет в конец каждой строки статус: 'отлично' если оценка >= 90, 'хорошо' если >= 75, иначе 'удовлетворительно'. 
# Сохрани результат в новый файл grades_with_status.txt.

with open('grades.txt', 'w') as f:
    f.write('Анна,85\nИван,72\nПётр,91')

def add_status(source: str, destination: str) -> None:
    with open(source, 'r') as f:
        lines = f.readlines()

    result = []
    for line in lines:
        line = line.strip()
        name, grade = line.split(',')
        grade = int(grade.strip())
        if grade >= 90:
            status = 'отлично'
        elif grade >= 75 and grade < 90:
            status = 'хорошо'
        else:
            status = 'удовлетворительно'
        result.append(f'{name},{grade},{status}\n')

    with open(destination, 'w') as f:
        f.writelines(result)

add_status('grades.txt', 'grades_with_status.txt')

# 3. Напиши функцию age_calculator(birth_date_str: str) -> int которая принимает дату рождения в формате 'dd/mm/yyyy' (input)  и возвращает полных лет. 

def age_calculator(birth_date_str: str) -> int:
    birth_date = datetime.strptime(birth_date_str, '%d/%m/%Y')
    today = datetime.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age  

print(age_calculator('15/08/1990'))


# 4.Напиши модуль file_utils.py с тремя полностью аннотированными функциями:

# def read_lines(filename): ...
# def write_lines(filename, lines): ...
# def count_words(filename): ... # count_words считает сколько раз каждое слово встречается в файле и возвращает словарь. 
# В main.py импортируй и протестируй все три.

# 5. Напиши функцию password_checker(correct_password) которая возвращает вложенную функцию check(password). Вложенная принимает пароль и возвращает True если совпадает, иначе False.

def password_checker(correct_password: str):
    def check(password: str) -> bool:
        return password == correct_password
    return check

print(password_checker('my_secret')('my_secret'))  # True
print(password_checker('my_secret')('wrong_password'))  # False 

