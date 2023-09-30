# Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)

new_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        new_matrix[j][i] = matrix[i][j]

print(new_matrix)