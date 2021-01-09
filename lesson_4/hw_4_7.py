def fact(n):
    f = 1
    for el in range(1, n + 1):
        f *= el
        yield f


for elm in fact(4):
    print(elm)
