# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# Matrix (двух матриц). Результатом сложения должна быть новая матрица.


class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def __str__(self):
        lines = []
        for row in self.rows:
            lines.append('\t'.join(map(str, row)))
        return '\n'.join(lines)

    def __add__(self, other):
        if self.compare(other):
            for i, row in enumerate(other.rows):
                for j, num in enumerate(row):
                    self.rows[i][j] += num
            return self
        else:
            return 'Матрицы не равны по размеру!'

    def compare(self, other):
        equal = True
        if type(other) == Matrix:
            if len(self.rows) != len(other.rows):
                equal = False
            else:
                for i, row in enumerate(other.rows):
                    if len(self.rows[i]) != len(other.rows[i]):
                        equal = False
                        break
        else:
            equal = False
        return equal


m1 = Matrix([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
m2 = Matrix([[6, 7, 8, 9, 10], [11, 12, 18, 19, 3], [16, 17, 18, 19, 14], [18, 29, 40, 32, 2]])
print(m1 + m2)
