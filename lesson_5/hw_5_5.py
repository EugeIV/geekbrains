from functools import reduce

with open("file_5_5.txt", "w", encoding="UTF-8") as my_file:
    my_file.write(input())

with open("file_5_5.txt", "r", encoding="UTF-8") as file_read:
    my_list = file_read.readline().split()
    sum_all = reduce(lambda x, y: int(x) + int(y), my_list)
    print(sum_all)