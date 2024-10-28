print('Задание №1')
number=int(input('Ведите целое число: '))
number=abs(number)
num=str(number)
summ=0
mult=1
for i in num:
    summ+=int(i)
    mult*=int(i)
print('Сумма цифр: ', summ)
print('Произведение цифр: ', mult)

print('Задание №2')
import math
X=float(input('Введите вещественное число:'))
N=int(input('Введите целое число, N>0 :'))
summ=1
for i in range(1,N+1):
    summ+=X**i/(math.factorial(i))
print('Полученное число является приближенным значением функции exp в точке X:', math.exp(X))

print('Задание №3')
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
A = int(input("Введите первое положительное число A: "))
B = int(input("Введите второе положительное число B: "))
if A > 0 and B > 0:
    result = gcd(A, B)
    print(f"Наибольший общий делитель {A} и {B} равен {result}.")
else:
    print("Пожалуйста, введите положительные целые числа.")