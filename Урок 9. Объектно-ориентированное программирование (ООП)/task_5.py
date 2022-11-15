class Stationery:
    title: str

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self):
        super().__init__()
        self.title = "ручка"

    def draw(self):
        print("Пишем текст")


class Pencil(Stationery):
    def __init__(self):
        super().__init__()
        self.title = "карандаш"

    def draw(self):
        print("Чертим чертеж")


class Handle(Stationery):
    def __init__(self):
        super().__init__()
        self.title = "маркер"

    def draw(self):
        print("Выделяем заголовки")


pen = Pen()
pencil = Pencil()
handle = Handle()
for some in [pen, pencil, handle]:
    print(f"{some.title}:")
    some.draw()
    print()
