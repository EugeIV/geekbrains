from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    print(el)

my_list = ["Hello", "my", "friends", "!"]
i = 0
for el in cycle(my_list):
    if i > 10:
        break
    print(el)
    i += 1
