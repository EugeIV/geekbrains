user_input = ""
total = 0

while user_input != "end":
    user_input = input("Введите числа через пробел или 'end' для выхода: ")
    list_input = user_input.split(" ")
    if "end" in list_input:
        total += sum([int(item) for item in list_input[:list_input.index("end")]], 0)
        break
    else:
        total += sum([int(item) for item in list_input], 0)
print(total)
