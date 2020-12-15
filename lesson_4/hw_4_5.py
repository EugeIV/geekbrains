from functools import reduce

my_list = [i for i in range(100, 1001) if i % 2 == 0]

sum_all = reduce(lambda x, y: x + y, my_list)
print(sum_all)
