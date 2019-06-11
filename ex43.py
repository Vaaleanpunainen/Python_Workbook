# program reads the denomination of a banknote from the user,
# then dosplays the name of the individual that appears on the banknote of the entered amount

denom = int(input("Enter the denomination of a banknote: "))

if denom == 1:
    name = "George Washington"
elif denom == 2:
    name = "Thomas Jefferson"
elif denom == 5:
    name = "Abraham Lincoln"
elif denom == 10:
    name = "Alexander Hamilton"
elif denom == 20:
    name = "Andrew Jackson"
elif denom == 50:
    name = "Ulysses S. Grant"
elif denom == 100:
    name = "Benjamin Franklin"
else:
    name = ""

if name == "":
    print("No such a denomination.")
else:
    print("The name of the individual that appears on the banknote $%s is %s." %(denom, name))
