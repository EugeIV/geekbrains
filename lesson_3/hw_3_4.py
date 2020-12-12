# Первый способ
def my_func_v1(x, y):
    return x ** y


# Второй спопсоб
def my_func_v2(x, y):
    z = x
    y = abs(y)
    while y > 1:
        z *= x
        y -= 1
    return 1 / z


print(my_func_v1(4, -3))
print(my_func_v2(4, -3))

