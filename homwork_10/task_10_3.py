class Cell:

    def __init__(self, nums):
        self.nums = nums

    def __str__(self):
        return f'cell {str(self.nums)}'

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        i = self.nums - other.nums
        return Cell(i) if i > 0 else f'вычитание данных клеток невозможно'

    def __mul__(self, other):
        return Cell(self.nums * other.nums)

    def __truediv__(self, other):
        return Cell(self.nums // other.nums)

    def make_order(self, row):
        return '\n'.join(['*' * row for _ in range(self.nums//row)]) + '\n' + '*' * (self.nums % row)

cell_1 = Cell(7)
cell_2 = Cell(2)
print(cell_1)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_2 / cell_1)
print(cell_1.make_order(2))



