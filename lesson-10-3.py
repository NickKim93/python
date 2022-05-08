class Cell:
    def __init__(self, qty):
        self.qty = qty

    def make_order(self, n):
        res = ['*' * n] * (self.qty // n)
        if self.qty % n:
            res.append('*' * (self.qty % n))
        return '\n'.join(res)

    def __str__(self):
        return f'Qty of cells: {self.qty}'

    def __add__(self, other):
        return Cell(self.qty + other.qty)

    def __sub__(self, other):
        if (self.qty - other.qty) > 0:
            return Cell(self.qty - other.qty)
        else:
            print('Value error')

    def __mul__(self, other):
        return Cell(self.qty * other.qty)

    def __floordiv__(self, other):
        return Cell(self.qty // other.qty)


cell_1 = Cell(40)
cell_2 = Cell(25000)
cell_sum = cell_1 * cell_2
print(cell_sum)
print(cell_1.make_order(7))
