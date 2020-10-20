# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться
# только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
# соответственно. В методе деления должно осуществляться округление значения до целого числа.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.


class Cell:
    def __init__(self, col):
        self.col = col

    def __str__(self):
        return f'Количество ячеек в клетке: {self.col}'

    def __add__(self, other):
        if type(other) == Cell:
            self.col += other.col
        return self

    def __sub__(self, other):
        if type(other) == Cell:
            sub = self.col - other.col
            if sub > 0:
                self.col = sub
                return self
            else:
                return 'Вычитание не возможно!'
        return self

    def __mul__(self, other):
        if type(other) == Cell:
            self.col *= other.col
        return self

    def __truediv__(self, other):
        if type(other) == Cell and other.col > 0:
            self.col //= other.col
        return self

    def make_order(self, num):
        string = ''
        for i in range(self.col):
            string += '*\n' if (i + 1) % num == 0 else '*'
        return string


c1 = Cell(24)
c2 = Cell(48)
c3 = Cell(35)
c4 = Cell(12)
c5 = Cell(10)

print(c1 + c2)
print(c1 - c3)
print(c1 * c4)
print(c1 / c5)
print(c1.make_order(12))
