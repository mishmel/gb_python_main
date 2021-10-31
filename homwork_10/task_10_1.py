class Matrix:
    def __init__(self, list_of_lists):
        self.lists = list_of_lists


    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.lists])

    def __add__(self, other):
        new_matrix = []
        if len(self.lists) != len(other.lists):
            return ('matrices of different sizes')
        else:
            for line, another in zip(self.lists, other.lists):
                if len(line) != len(another):
                    return ('matrix elements of different sizes')
                else:
                    z = [x + y for x, y in zip(line, another)]
                    new_matrix.append(z)
        return '\n'.join([' '.join(map(str, line)) for line in new_matrix])


matrix_1 = Matrix([[1, 2],[2, 3]])
matrix_2 = Matrix([[5, 6],[7, 8]])
matrix_3 = Matrix([[5, 6, 9]])

print(matrix_1)
print()
print(matrix_1 + matrix_2)
print(matrix_1 + matrix_3)

