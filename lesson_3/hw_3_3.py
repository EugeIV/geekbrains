# Первый вариант
def my_func_1(arg1, arg2, arg3):
    return (arg1 + arg2 + arg3) - min(arg1, arg2, arg3)


# Второй, но более длинный вариант

def my_func_2(arg1, arg2, arg3):
    l = [arg1, arg2, arg3]
    l.sort()
    return l[1] + l[2]


print(my_func_1(12, 3, 7))
print(my_func_2(12, 3, 7))
