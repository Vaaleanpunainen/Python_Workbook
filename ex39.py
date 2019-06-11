# program reads a value of sound in decibeles from the user,
# then displays message about sound level


db =  int(input("Enter the sound level in decibeles: "))

if db == 130:
    level = "jackhammer"
elif 106 < db < 130:
    level = "beetween jackhammer and gas lawnower"
elif db == 106:
    level = "gas lawnmower"
elif 70 < db < 106:
    level = "beetween gas lawnmower and alarm clock"
elif db == 70:
    level = "alarm clock"
elif 40 < db < 70:
    level = "beetween alarm clock and quiet room"
elif db == 40:
    level = "quiet room"
else:
    level = ""

if level == "":
    if db < 40:
        print("The value is smaller than the quiet room noise.")
    elif 130 < db:
        print("The value is larger than the jackhammer noise.")
else:
    print("", level)
