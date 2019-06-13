# program reads a message from the user,
# then implements a Cesar cipher

message = input("Enter the message: ")
shifts = int(input("Enter the value of shifts: "))

cipher = ""

for l in message:
    if l >= "a" and l <= "z":
        pos = ord(l) - ord("a")
        pos = (pos + shifts) % 26
        new_l = chr(pos + ord("a"))
        cipher = cipher + new_l
    elif l >= "A" and l <= "Z":
        pos = ord(l) - ord("A")
        pos = (pos + shifts) % 26
        new_l = chr(pos + ord("A"))
        cipher = cipher + new_l
    else:
        cipher = cipher + l

print("Your shifted message is:", cipher)
