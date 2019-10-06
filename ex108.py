# program sort numbers in three groups: negatives, zeros and positives
# and displays them in the same order that they were entered by the user

number = input("Enter a number (blank line to exit): ")
negatives = []
zeros = []
positives = []

while number != "":
    number = int(number)
    if number < 0:
        negatives.append(number)
    elif number == 0:
        zeros.append(number)
    elif number > 0:
        positives.append(number)
    number = input("Enter a number (blank line to exit): ")

for n in negatives:
    print(n)
for z in zeros:
    print(z)
for p in positives:
    print(p)
