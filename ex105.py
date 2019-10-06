# Program reads integers from the user and stores them in a list until the user enters 0,
# then displays all of the entered vaues (except for the 0) in reverse order,
# with one value appearing on each line

list = []
i = 1
while i != 0:
    i = int(input("Enter a number: "))
    if i != 0:
        list.append(i)
    else:
        list.reverse()

print("Your inputs in reverse order: ")
for l in list:
    print(l)
