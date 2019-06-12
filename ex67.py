# programs computes the price of admission based on the age of the guest

sm = 0

age = input("Enter the age of guest: ")

while age != "":
    age = int(age)
    if age <= 2:
        cost = 0.00
    elif 3 <= age <=12:
        cost = 14.00
    elif 65 <= age:
        cost = 18.00
    else:
        cost = 23.00
    sm += cost

    age = input("Enter the age of guest (blank to quit): ")

print("The total cost of all guest: $%s" %sm)
