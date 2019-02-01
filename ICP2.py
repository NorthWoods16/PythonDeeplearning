for integer in range(100, 500):
    intStr = str(integer)[0]
    if int(intStr) % 2 == 1:
        intStr = str(integer)[1]
        if int(intStr) % 2 == 1:
            intStr = str(integer)[2]
            print(integer)

myList = ["1", "4", "0", "6", "9"]
myList.sort()
print(myList)

fileName = input("file name\n")
in_file = open(fileName, "r")
words = 0
characters = -1
line = "start"
while line != "":
    line = in_file.readline()
    for word in line.split(' '):
        words+=1
        for char in word:
            characters+=1
print(words, characters)