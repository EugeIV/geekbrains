# Первый способ
# season = ["зима", "весна", "лето", "осень"]

# month = int(input("Введите число месяца: "))
# if month in range(3, 6):
#     print(season[1])
# elif month in range(6, 9):
#     print(season[2])
# elif month in range(9, 12):
#     print(season[3])
# elif month == 12 or month in range(1, 3):
#     print(season[0])
# else:
#     print("Нет такого месяца!")

# Второй способ (больше подходит для месяцев)
# season = {1: "зима",
#           2: "зима",
#           3: "весна",
#           4: "весна",
#           5: "весна",
#           6: "лето",
#           7: "лето",
#           8: "лето",
#           9: "осень",
#           10: "осень",
#           11: "осень",
#           12: "зима"}
#
# month = int(input("Введите число месяца: "))
# if 1 <= month <= 12:
#     print(season[i])
# else:
#     print("Нет такого месяца!")

# Третий способ (самый оптимальный, долго разбирался как обратиться к числам в списке)
season = {"весна": [3, 4, 5],
          "лето": [6, 7, 8],
          "осень": [9, 10, 11],
          "зима": [12, 1, 2]}
month = int(input("Введите число месяца: "))
output = ""
for item in season:
    if month in season[item]:
        output = item
        break
    else:
        output = "Нет такого месяца!"
print(output)
