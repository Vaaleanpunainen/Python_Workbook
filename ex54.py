# program reads a wavelenght from the user,
# then reports its colour

wavelenght = int(input("Enther the wavelenght: "))

if 380 <= wavelenght < 450:
    colour = "violet"
elif 450 <= wavelenght < 495:
    colour = "blue"
elif 495 <= wavelenght < 570:
    colour = "green"
elif 570 <= wavelenght < 590:
    colour = "yellow"
elif 590 <= wavelenght < 620:
    colour = "orange"
elif 620 <= wavelenght <= 750:
    colour = "red"
else:
    colour = ""

if colour == "":
    print("The entered wavelenght is outside of the visible spectrum.")
else:
    print("The wavelenght %s nm has %s colour." %(wavelenght, colour))
