def equal(N, S):

    if N == 0:
        return S == 0
    else:
        return equal(N // 10, S - (N % 10))

def is_non_negative_integer(value):

    try:
        int_value = int(value)
        return int_value >= 0
    except ValueError:
        return False

def get_non_negative_integer(prompt):

    while True:
        value = input(prompt)
        if is_non_negative_integer(value):
            return int(value)
        else:
            print("Ошибка ввода: введите неотрицательное целое число.")

N = get_non_negative_integer("Введите неотрицательное целое число N: ")
S = get_non_negative_integer("Введите неотрицательное целое число S: ")

result = equal(N, S)

print(f"Сумма цифр числа {N} {'равна' if result else 'не равна'} {S}.")
