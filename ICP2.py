start = input("Enter starting number\n")
end = input("Enter ending number\n")
for integer in range(int(start), int(end)):
    for idx in range(0, len(str(integer))):
        intStr = str(integer)[idx]
        if int(str(integer)[idx]) % 2 == 0:
            break
        elif idx == int(len(str(integer)) - 1):
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