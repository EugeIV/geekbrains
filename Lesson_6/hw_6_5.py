class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationery):
    def draw(self):
        return f"Рисует {self.title}"


class Pencil(Stationery):
    def draw(self):
        return f"Рисует {self.title}"


class Handle(Stationery):
    def draw(self):
        return f"Рисует {self.title}"


pen = Pen("ручка")
print(pen.draw())
pencil = Pencil("карандаш")
print(pencil.draw())
handle = Handle("маркер")
print(handle.draw())