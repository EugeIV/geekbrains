my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("file_5_4.txt", "r", encoding="UTF-8") as file_in:
    for line in file_in:
        line = line.split(' ', 1)
        with open("out_file_5_4.txt", "a", encoding="UTF-8") as file_out:
            file_out.write(my_dict[line[0]] + ' ' + line[1])
