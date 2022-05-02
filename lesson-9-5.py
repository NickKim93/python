class Stationery:

    def __init__(self, title='Что-то рисуем'):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Теперь рисуем карандашом {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Начинаем отрисовку ручкой {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем маркером {self.title}')


pen = Pen('Гелиевая ручка')
pen.draw()
pencil = Pencil('ТН Карандаш')
pencil.draw()
marker = Handle('Белый маркер')
marker.draw()
