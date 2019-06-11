# program reads the note's frequency from the user,
# then displays the name of the note

freq = float(input("Enter the note's frequency: "))

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

if C4 - 1 <= freq <= C4 + 1:
    note = "C4"
elif D4 - 1 <= freq <= D4 + 1:
    note = "D4"
elif E4 - 1 <= freq <= E4 + 1:
    note = "E4"
elif F4 - 1 <= freq <= F4 + 1:
    note = "F4"
elif G4 - 1 <= freq <= G4 + 1:
    note = "G4"
elif A4 - 1 <= freq <= A4 + 1:
    note = "A4"
elif B4 - 1 <= freq <= B4 + 1:
    note = "B4"
else:
    note = ""

if note == "":
    print("There is no note that corresponded this frequency.")
else:
    print("The frequency %s is note %s" %(freq, note))
