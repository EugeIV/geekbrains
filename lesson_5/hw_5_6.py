my_dict = {}

with open("file_5_6.txt", "r", encoding="UTF-8") as my_file:
    for line in my_file:
        sub, lec, prac, lab = line.split()
        hour_list = [lec[:lec.find('(')], prac[:prac.find('(')], lab[:lab.find('(')]]
        sum_hour = 0
        for i in hour_list:
            if i != "":
                sum_hour += int(i)
        my_dict[sub] = sum_hour

print(my_dict)
