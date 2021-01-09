class Matrix:

    def __init__(self, matrix: [[]]):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % el for el in row]) for row in self.matrix])

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.matrix)):
            new_matrix.append([])
            for j in range(len(other.matrix[i])):
                new_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(new_matrix)


print((Matrix([[1, 2, 3], [2, 3, 4], [3, 3, 3]]) + Matrix([[1, 2, 3], [2, 3, 4], [3, 3, 3]]))
      == Matrix([[2, 4, 6], [4, 6, 8], [6, 6, 6]]))
# matrix_3x3 = Matrix([[1, 2, 3], [2, 3, 4], [3, 3, 3]])
# matrix_3x3_2 = Matrix([[1, 2, 3], [2, 3, 4], [3, 3, 3]])
# print("Первая матрица")
# print(matrix_3x3)
# print("Вторая матрица")
# print(matrix_3x3_2)
# print("Сумма матриц")
# print(matrix_3x3 + matrix_3x3_2)
# print("-" * 10)
# print("Первая матрица")
# print(matrix_3x3)
# print("Вторая матрица")
# print(matrix_3x3_2)
