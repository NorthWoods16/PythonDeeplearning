x = input("Enter a 3 digit number")
print(x[::-1])

x = input("enter number")
y = input("enter number")

print("%s times %s equals %s" %(x, y, int(x)*int(y)))

x = input("enter a sentence")
letters = 0
words = 1
numbers = 0
for i in range(len(x)):
    if x[i].isalpha():
        letters+=1
    if x[i].isspace():
        words+=1
    if x[i].isnumeric():
        numbers+=1
print("Letters: %i Words: %i Numbers: %i" %(letters, words, numbers))