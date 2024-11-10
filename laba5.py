print('Задание №1')
while True:
    try:
        number= int(input("Введите целое число: ", ))
        break
    except ValueError:
        print(" Попробуй ещё раз, спасибо!")
number=abs(number)
num=str(number)
summ=0
mult=1
for i in num:
    summ+=int(i)
    mult*=int(i)
print('Сумма цифр: ', summ)
print('Произведение цифр: ', mult)

('Задание №2')
import math
while True:
    while True:
       try: N= float(input('Введите вещественное число X: '))
       except ValueError:
           print('Пожалуйста, попробуйте еще раз,спасибо!')
       else: break
    if N <= 0:
        print('Введено неположительное число')
    else: break
while True:

    while True:
       try: N= int(input('Введите целое число, N>0: '))
       except ValueError:
           print('Пожалуйста, попробуйте еще раз,спасибо!')
       else: break
    if N <= 0:
        print('Введено неположительное число')
    else: break
summ=1
for i in range(1,N+1):
    summ+=X**i/(math.factorial(i))
print('Полученное число является приближенным значением функции exp в точке X:', math.exp(X))
print('Задание №3')
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
while True:
    while True:
       try: A= int(input('Введите первое положительное число A: '))
       except ValueError:
           print('Пожалуйста, попробуйте еще раз,спасибо!')
       else: break
    if A <= 0:
        print('Введено неположительное число')
    else: break
while True:
    while True:
        try:
            B= int(input('Введите второе положительное число B: '))
        except ValueError:
            print('Пожалуйста, попробуйте еще раз,спасибо!')
        else:
            break
    if B <= 0:
        print('Введено неположительное число')
    else:
        break

result = gcd(A, B)
print(f"Наибольший общий делитель {A} и {B} равен {result}.")