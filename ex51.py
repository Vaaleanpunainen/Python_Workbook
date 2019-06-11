# program reads a letter grade from the user
# then displays the equivalent number of grade points


letter = (input("Enter a letter grade: ")).upper()

if letter == "A-":
    gp = 3.7
elif letter[0] == "A":
    gp = 4.0
elif letter == "B+":
    gp = 3.3
elif letter == "B":
    gp = 3.0
elif letter == "B-":
    gp = 2.7
elif letter == "C+":
    gp = 2.3
elif letter == "C":
    gp = 2.0
elif letter == "C-":
    gp = 1.7
elif letter == "D+":
    gp = 1.3
elif letter == "D":
    gp = 1.0
elif letter == "F":
    gp = 0
else:
    gp = "error"

if gp == "error":
    print("Invalid letter grade.")
else:
    print("The equivalent number of grade points is %s" %gp)
