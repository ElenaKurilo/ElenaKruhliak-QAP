
# Привести к целому типу - 1.6, 2.99
number_1 = int(1.6)
number_2 = int(2.99)
print(number_1, number_2)

# Заменить символ "#" на символ "/" в строке 'www.my_ site.com#about'
text = "www.my_ site.com#about"
text = text.replace("#", "/")
print(text)

# Напишите программу, которая добавляет 'ing' к слову 'stroka'
word = "stroka"
word += "ing"
print(word)

# В строке "Ivanou Ivan" поменяйте местами слова => "Ivan Ivanou"
name = "Ivanou Ivan"
name = name.split()
name[0], name[1] = name[1], name[0]
name = " ".join(name)   
print(name)

# Напишите программу которая удаляет пробел в начале, в конце строки
text = "   Hello, World!   "
text = text.strip()
print(text)

# Создайте словарь, связав его с переменной school, и наполните его данными,
# которые бы отражали количество учащихся в десяти разных классах
# (например, 1а, 1б, 2б, 4а, 7в и т.д.)
school = {
    "1а": 15,
    "1б": 20,
    "2б": 27,
    "4а": 24,
    "4г": 19,
    "5а": 28,
    "5в": 30,
    "7в": 22
}
print(school)

# Создайте список и извлеките из него списка второй элемент
my_list = [10, "cat", 30, 2.99, {}]
print(my_list[1])

# Вывести входит ли строка 1 в строку2 (пример: employ и employment )
text1 = "employ"
text2 = "employment"
print(text1 in text2)

# Вывести нужные символы
# x = "My name is Agent Smith"
# print(x[1])  # y
# print(x[3:16:3])  # nesgt
text = "My name is Agent Smith"
print (text[1])
print(text[3:16:3])

# Есть массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5.
# Напишите программу, которая будет выводить уникальное число.
numbers = [1, 5, 2, 9, 2, 9, 1]
for number in numbers:
    if numbers.count(number) == 1:        
        print(number)        
        break
