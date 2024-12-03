print('№1')
import random

while True:
    size_input=input('Введите размер матрицы: ')
    try:
        size=int(size_input)
        if size>0:
            break
        else:
            print("Размер матрицы должен быть положительным. Пожалуйста, введите еще раз!")
    except ValueError:
        print('Некорректный ввод.Пожалуйста, введите целое число!')

matr=[]

for i in range(size):
    row=[]
    for j in range(size):
        row.append(random.randint(-10,10))
    matr.append(row)

print('Сгенерированная матрица: ')
for row in matr:
    print(row)

negative_count=0

for i in range(size):
    for j in range(size):
        if ((i + j) > (size - 1)) and matr[i][j]<0 :
            negative_count +=1

print(f'Количество отрицательных элементов ниже побочной диагонали: {negative_count}')



print('№2')
import random

size = 8
matr = []

for i in range(size):
    row = []
    for j in range(size):
        row.append(random.randint(0, 1))
    matr.append(row)


print('Сгенерированная матрица: ')
for row in matr:
    print(row)

index_ = []


for k in range(size):
    match = True
    for i in range(size):
        if matr[k][i] != matr[i][k]:
            match = False
            break
    if match:
        index_.append(k)


print(f'Индексы k, где k-я строка совпадает с k-м столбцом: {index_}')



print('№3')
import random

while True:
    try:
        size = int(input("Введите размер строки : "))
        if size <= 0:
            print("Введите положительное целое число.")
        else:
            break
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")


random_numbers = []

for i in range(size):
    number = random.randint(0,9)
    random_numbers.append(number)

print("Сгенерированная строка чисел:", random_numbers)


number_count = {}
for number in random_numbers:
    if number in number_count:
        number_count[number] += 1
    else:
        number_count[number] = 1

print("Словарь с количеством повторений чисел:", number_count)


while True:
    user_input = input("Введите число от 0 до 9 для поиска его повторений: ")
    try:
        number_to_find = int(user_input)
        if 0 <= number_to_find <= 9:
            count = number_count.get(number_to_find, 0)
            print(f"Число {number_to_find} встречается {count} раз(а) в строке.")
            break
        else:
            print("Введите число в диапазоне от 0 до 9.")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")