def int_func(user_input):
    return user_input.title()


# Через capitalize (от преподавателя)
def int_func_2(user_input):
    return user_input.capitalize()


text = input("Введите слово или строку: ")
print(int_func(text))
print(' '.join(map(int_func_2, text.split())))
