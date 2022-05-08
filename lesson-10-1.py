class Matrix:
    def __init__(self, a):
        self.A = a

    def __str__(self):
        mtx = ''
        for i in range(len(self.A)):
            mtx += (''.join(map(lambda x: '{:4d}'.format(x), self.A[i])) + '\n')
        return mtx

    def __add__(self, other):
        new_mtx = Matrix(self.A)
        for i in range(len(self.A)):
            for j in range(len(self.A[i])):
                new_mtx.A[i][j] = self.A[i][j] + other.A[i][j]
        return new_mtx


matrix_1 = Matrix([[11, 23, 333], [2, 3, 12]])
matrix_2 = Matrix([[3, 25, 33], [4, 2, 5]])
print(matrix_1)
matrix_sum = matrix_1 + matrix_2
print(matrix_1)  #    Почему после сложения, matrix_1 становится равным matrix_sum?
print(matrix_2)
print(matrix_sum)
