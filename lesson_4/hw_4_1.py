from sys import argv

script_salary, working_hours, rate_per_hour, premium = argv

print("Имя скрипта: ", script_salary)
print("Зарплата сотрудника: ", int(working_hours) * int(rate_per_hour) + int(premium))
