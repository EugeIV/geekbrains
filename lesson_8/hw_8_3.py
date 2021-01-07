class MyException(Exception):
    def __init__(self, text):
        self.text = text


my_list = []

while True:
    i = input()
    if i == "stop":
        break
    try:
        if not i.isdigit():
            raise MyException("Введено не число")
        my_list.append(i)
    except MyException as err:
        print(err)
print(my_list)
