# Мое решение

# my_list = [7, 5, 3, 3, 2, int(input())]
# new_my_list = sorted(my_list)
# new_my_list.reverse()
# print(new_my_list)


# Решение от преподавателя

my_list_2 = [9, 8, 7, 7, 6, 5, 3, 1]
new_number = int(input("Enter the new number: "))
i = 0
for n in my_list_2:
    if new_number <= n:
        i += 1
my_list_2.insert(i, new_number)
print(my_list_2)
