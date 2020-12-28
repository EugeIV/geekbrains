class Cell:

    def __init__(self, quantity: int):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return self.quantity - other.quantity
        else:
            return "Отрицательное число клеток"

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def make_order(self, row):
        result = ""
        for i in range(self.quantity // row):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


a = Cell(33)
c = Cell(100)
print(a + c)
print(c - a)
print(a * c)
try:
    print(c / a)
except ZeroDivisionError:
    print("Деление на ноль")
print(a.make_order(10))
