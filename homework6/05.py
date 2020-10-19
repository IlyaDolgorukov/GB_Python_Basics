# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title}. Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self):
        super().__init__('Ручка')

    def draw(self):
        print(f'{self.title} пишет.')


class Pencil(Stationery):
    def __init__(self):
        super().__init__('Карандаш')

    def draw(self):
        print(f'{self.title} рисует.')


class Handle(Stationery):
    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        print(f'{self.title} выделяет текст.')


stylus = Stationery('Стилус')
stylus.draw()
print()

pen = Pen()
pen.draw()
print()

pencil = Pencil()
pencil.draw()
print()

handle = Handle()
handle.draw()
print()
