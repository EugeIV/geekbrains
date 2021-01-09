class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f"Сумма комплексных чисел: {self.a + other.a} + {self.b + other.b}i"

    def __mul__(self, other):
        return f"Произведение комплексных чисел: " \
            f"{(self.a * other.a) - (self.b * other.b)} + {(self.b * other.a) + (self.a * other.b)}i"


z_1 = ComplexNumber(3, -4)
z_2 = ComplexNumber(5, 7)
print(z_1 + z_2)
print(z_1 * z_2)
