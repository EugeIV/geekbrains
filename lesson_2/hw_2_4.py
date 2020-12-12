inputUser = input()
listOfWords = inputUser.split(" ")
count = 1
for word in listOfWords:
    print(f"{count}. {word[:10]}")
    count += 1
