with open("file_5_3.txt", "r", encoding="UTF-8") as my_file:
    name_20000 = []
    sum_salary = 0
    employee = 0
    for line in my_file:
        if int(line.split()[1]) <= 20000:
            name_20000.append(line.split()[0])
        sum_salary += int(line.split()[1])
        employee += 1

print("Сотрудники с зарплатой менее 20000: ")
for n in name_20000:
    print("-" * 5, n, "-" * 5)

print(f"Средняя зарплата по сотрудникам: {sum_salary / employee: .2f}")
