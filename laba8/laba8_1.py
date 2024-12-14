import math

def TriangleP(a, h):

    b = math.sqrt((a / 2) ** 2 + h ** 2)
    perimeter = a + 2 * b
    return perimeter

def is_float(value):

    value = value.replace(',', '.')
    try:
        float(value)
        return '.' in value
    except ValueError:
        return False

def get_positive_float(prompt):

    while True:
        value = input(prompt)
        if is_float(value):
            value = float(value.replace(',', '.'))
            if value > 0:
                return value
            print("Ошибка: значение должно быть положительным.")
        else:
            print("Ошибка ввода: введите корректное вещественное число с целой и дробной частью.")

triangles = []

for i in range(3):
    print(f"\nВвод данных для треугольника {i + 1}:")

    h = get_positive_float("Введите высоту: ")

    while True:
        a = get_positive_float("Введите основание: ")
        if a > h:
            break
        else:
            print("Ошибка: основание должно быть больше высоты. Пожалуйста, попробуйте снова.")

    triangles.append((a, h))

i = 1

for triangle in triangles:
    a, h = triangle
    perimeter = TriangleP(a, h)
    print(f"Периметр треугольника {i+1} с основанием {a} и высотой {h}: {perimeter:.2f}")
