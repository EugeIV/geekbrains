num = int(input("Enter the number: "))
maximum = 0
while num != 0:
    n = num % 10
    if n > maximum:
        maximum = n
    num = num // 10
print(maximum)
