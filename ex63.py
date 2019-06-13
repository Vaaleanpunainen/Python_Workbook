print("    ", end="")

for i in range(1):
    print("*C", "  ", "*F", end="\t")

print("^")

for C in range(0,101):
    print("%4d" % C, end="*C")
    for F in range (1):
        print("%4d" % (C * 9/5 + 32), end="*F")
    print("")
