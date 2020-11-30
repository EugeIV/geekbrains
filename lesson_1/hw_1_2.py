time = int(input("Enter the time in second: "))
hour = time // 3600
minute = time % 3600 // 60
second = time % 3600 % 60
print("%02d:%02d:%02d" % (hour, minute, second))
