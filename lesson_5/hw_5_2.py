with open("file_5_2.txt", encoding="UTF-8") as f_obj:
    print(f"В тексте - {len(f_obj.readlines())} строк(и)")
print()

with open("file_5_2.txt", encoding="UTF-8") as f_obj:
    count = 0
    for line in f_obj:
        count += 1
        print(f"{count} строка - {len(line.split(' '))} слов(а)")
