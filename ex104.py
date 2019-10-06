# Program reads integers from the user and stores them in a list until the user enters 0,
# then displays all of the entered vaues (except for the 0) in order from smallest to largest,
# with one value appearing on each line

list = []
i = 1
while i != 0:
    i = int(input("Enter a number (0 to exit): "))
    if i != 0:
        list.append(i)
    else:
        list.sort()

print("Your sorted inputs: ")
for l in list:
    print(l)
