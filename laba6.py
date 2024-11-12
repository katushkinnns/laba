# Задание 1
user_input = input('Введите текст: ')

english_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

valid_characters = english_alphabet + russian_alphabet + ' '

while True:
    is_empty = True
    for char in user_input:
        if char != ' ':
            is_empty = False
            break

    if is_empty:
        user_input = input('Введена пустая строка. Пожалуйста, введите текст: ')
        continue

    valid_input = True
    for c in user_input:
        if c not in valid_characters:
            valid_input = False
            break

    if valid_input:
        break
    else:
        user_input = input('Неверный формат ввода. Пожалуйста, введите текст: ')


gl = 'aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ'
count=0
in_word = False
for i in range(len(user_input)):
    if user_input[i] != ' ':
        if not in_word:
            in_word = True
            if user_input[i] in gl:
                count += 1
    else:
        in_word = False
print(f'Кол-во слов текста, которые начинаются с гласной буквы равно: {count}')


#Задание 2
text = input('Введите текст: ')
numbers = '1234567890.-'

while True:
    valid_input = False
    for num in numbers:
        if num in text:
            valid_input = True
            break
    if valid_input:
        break
    else:
        text = input('Неверный формат ввода. Введите текст: ')

numbers_lst = []
first_numbers = ""
is_float = False
is_negative = False

for i, char in enumerate(text):
    if char in '0123456789':
        first_numbers += char
    elif char == '-' and (i == 0 or text[i - 1] in ' ,'):
        is_negative = True
    elif char == '.' and not is_float:
        first_numbers += char
        is_float = True
    else:
        if first_numbers:
            if is_float:
                number = float(first_numbers)
            else:
                number = int(first_numbers)

            if is_negative:
                is_negative = False

            numbers_lst.append(number)
            first_numbers = ""
            is_float = False

if first_numbers:
    if is_float:
        number = float(first_numbers)
    else:
        number = int(first_numbers)

    if is_negative:
        number = -number

    numbers_lst.append(number)

print("Найденные числа:", numbers_lst)


# Задание 3
import random
from random import randint

while True:
    try:
        size = int(input('Введите размер списка: '))
        if size <= 0:
            print('Размер должен быть положительным целым числом')
            continue
        break
    except ValueError:
        print('Неверный формат ввода. Повторите ввод.' )

random_list = [random.randint(-10, 10) for _ in range(size)]
print('Исходный список:', random_list)

first_index = -1
second_index = -1
for i in range(len(random_list)):
    if random_list[i] > 0:
        if first_index == -1:
            first_index = i
        elif second_index == -1:
            second_index = i
            break

if first_index != -1 and second_index != -1 and second_index > first_index + 1:
    res = 0
    for i in range(first_index + 1, second_index):
        res += random_list[i]
    print(f'Индексы элементов: Первый - {first_index}, Второй - {second_index}')
else:
    res = 0
    print('Недостаточно элементов для вычисления суммы.')

print('Сумма элементов между первым и вторым элементом:', res)

lst_zero = [i for i in random_list if i != 0] + [i for i in random_list if i == 0]
print('Измененный список (нули перемещены в конец списка):', lst_zero)