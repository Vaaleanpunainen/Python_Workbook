# program computes parity for sets of 8 bits by enter user

line = input("Enter 8 bits (blank line to quit): ")

while line != "":
    if line.count("0") + line.count("1") != 8 or len(line) != 8:
        print("Wrong enter.")
    else:
        ones = line.count("1")
        if ones % 2 == 0:
            print("The parity bit should be 0.")
        else:
            print("The parity bit should be 1.")

    line = input("Enter 8 bits (blank line to quit): ")

print("Program ends.")
