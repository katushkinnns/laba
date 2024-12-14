import random

def generate_matrix(rows, cols):

    return [[random.uniform(-10, 10) for _ in range(cols)] for _ in range(rows)]

def find_min_element(matrix):

    min_value = matrix[0][0]
    min_position = (0, 0)

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            value = matrix[i][j]
            if value < min_value:
                min_value = value
                min_position = (i, j)

    return min_value, min_position

rows_A = 5
cols_A = 10
rows_B = 10
cols_B = 4

A = generate_matrix(rows_A, cols_A)
B = generate_matrix(rows_B, cols_B)

min_value_A, position_A = find_min_element(A)
min_value_B, position_B = find_min_element(B)

print("Матрица A:")
for row in A:
    print(row)

print(
    f"\nНаименьший элемент в матрице A: {min_value_A} на позиции (строка: {position_A[0] + 1}, столбец: {position_A[1] + 1})")

print("\nМатрица B:")
for row in B:
    print(row)

print(
    f"\nНаименьший элемент в матрице B: {min_value_B} на позиции (строка: {position_B[0] + 1}, столбец: {position_B[1] + 1})")
