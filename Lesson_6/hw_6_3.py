class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{self._income['wage'] + self._income['bonus']} рублей"


ivan = Position(name="Иван", surname="Кузнецов", position="менеджер", wage=35000, bonus=3500)
print(ivan.get_full_name())
print(ivan.get_total_income())
