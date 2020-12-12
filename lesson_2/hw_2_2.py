l = []
while True:
    i = input()
    if i == "":
        break
    l.append(i)
print("Исходный список: ", l)

if len(l) % 2 == 0:
    for x in range(0, len(l), 2):
        l[x], l[x + 1] = l[x + 1], l[x]
else:
    for x in range(0, len(l)-1, 2):
        l[x], l[x + 1] = l[x + 1], l[x]

print("Новый список: ", l)
