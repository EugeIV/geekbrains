goods = []

while input("Хотите добавить еще товар (да/нет)? ") == "да":
    number = int(input("Введите номер товара: "))
    structure = {}
    while input("Добавить параметр товара (да/нет)? ") == "да":
        structure_key = input("Введите параметр: ")
        structure_value = input("Введите значение: ")
        structure[structure_key] = structure_value
    goods.append(tuple([number, structure]))
print(goods)

analytics = {}
for good in goods:
    for structure_key, structure_value in good[1].items():
        if structure_key in analytics:
            analytics[structure_key].append(structure_value)
        else:
            analytics[structure_key] = [structure_value]
print(analytics)
