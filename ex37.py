# program reads the number of sides from the user,
# then report the appropriate name as part of a meaningful message

sides = int(input("Enter the number of sides: "))

if sides == 3:
    print("It is a triangle!")
elif sides == 4:
    print("It is a rectangle!")
elif sides == 5:
    print("It is a pentagon!")
elif sides == 6:
    print("It is a hexagon!")
elif sides == 7:
    print("It is a heptagon!")
elif sides == 8:
    print("It is a octagon!")
elif sides == 9:
    print("It is a nonagon!")
elif sides == 10:
    print("It is a decagon!")
else:
    print("No such a shape!")
