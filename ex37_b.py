# program reads the number of sides from the user,
# then report the appropriate name as part of a meaningful message

sides = int(input("Enter the number of sides: "))

if sides == 3:
    name = "triangle"
elif sides == 4:
    name = "rectangle"
elif sides == 5:
    name = "pentagon"
elif sides == 6:
    name = "hexagon"
elif sides == 7:
    name = "heptagon"
elif sides == 8:
    name = "octagon"
elif sides == 9:
    name = "nonagon"
elif sides == 10:
    name = "decagon"
else:
    name = ""

if name == "":
    print("We have no such a shape in our database.")
else:
    print("This shape is %s" %name)
