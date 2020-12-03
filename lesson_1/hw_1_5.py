revenue = int(input("Введите значение выручки: "))
costs = int(input("Введите издержки: "))
profit = revenue - costs
profitability = profit / revenue

if profit > 0:
    print("Фирма работает с прибылью")
    print("Рентабельность: %.3f" % (profitability))
    staff = int(input("Введите количество сотрудников: "))
    print("Прибыль на одного сотрудника: ", profit // staff)
elif profit == 0:
    print("Фирма работает в 0")
else:
    print("Фирма работает с убытками")
