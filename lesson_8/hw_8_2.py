class MyException(Exception):
    def __init__(self, text):
        self.text = text


def division(a, b):
    if not b:
        raise MyException("Делить на ноль нельзя!")
    return a / b


try:
    print(division(1, 0))
except MyException as err:
    print(err)
