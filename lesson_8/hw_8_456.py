from abc import ABC, abstractmethod


class Equipment(ABC):
    def __init__(self, name: str, serial_number: int):
        if type(serial_number) != int:
            raise ValueError("Invalid serial number value!")
        self.name = name
        self.serial_number = serial_number
        self.department = None

    def _set_department(self, department):
        self.department = department

    @abstractmethod
    def __str__(self):
        pass


class Printer(Equipment):
    def __str__(self):
        return f"Printer {self.name}, serial number {self.serial_number}."

    def print(self, data: str):
        return f"Printer {self.name} printed {data}"


class Scanner(Equipment):
    def __str__(self):
        return f"Scanner {self.name}, serial number {self.serial_number}."

    def scan(self, data: str):
        return f"Scanner {self.name} scans {data}"


class Xerox(Equipment):
    def __str__(self):
        return f"Xerox {self.name}, serial number {self.serial_number}."

    def copy(self, data: str):
        return f"Xerox {self.name} copy {data}"


class Warehouse:
    def __init__(self):
        self.storage = {"printers": set(),
                        "scanners": set(),
                        "xeroxes": set()}
        self.add_mapper = {Printer: "printers",
                           Scanner: "scanners",
                           Xerox: "xeroxes"}
        self.total = 0

    def get_to_the_warehouse(self, equipment: Equipment):
        self.storage[self.add_mapper[type(equipment)]].add(equipment)
        equipment._set_department("warehouse")
        self.total += 1

    def __call__(self, *args, **kwargs):
        self.get_to_the_warehouse(*args, **kwargs)

    def send_to_the_department(self, type_equipment, department):
        equipment_to_send = self.storage[type_equipment].pop()
        equipment_to_send._set_department(department)
        self.total -= 1


printer_1 = Printer("HP", 123)
print(printer_1)
print(printer_1.department)
warehouse = Warehouse()
warehouse(printer_1)
print(printer_1.department)
warehouse.send_to_the_department("printers", "marketing")
print(printer_1.department)
