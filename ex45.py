# program reads a position from the user,
# then displays if the square is black or white

position = (input("Enter the posiotion (i.e. a1): ")).lower()

first_black = ("a", "c", "e", "g")
first_white = ("b", "d", "f", "h")

if position[0] in first_black:
    colour = "black"
else:
    colour = "white"

if int(position[1])%2 == 0:
    number = "even"
else:
    number = "odd"

if colour == "black" and number == "odd":
    print("%s square is black" %position)
elif colour == "black" and number == "even":
    print("%s square is white" %position)
elif colour == "white" and number == "odd":
    print("%s square is white" %position)
elif colour == "white" and number == "even":
    print("%s square is black" %position)
