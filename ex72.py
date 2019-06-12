# program reads a string from the user,
# determines whether or not is a palindrome

line1 = input("Enter a string: ")

lenght = len(line1) - 1

line2 = ""

while lenght >= 0:
    line2 = line2 + line1[lenght]
    lenght = lenght - 1

if line1 == line2:
    print("The word %s is a palindrome." %line1)
else:
    print("The word '%s' is not a palindrome." %line1)
