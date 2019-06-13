for row in range(0, 11):
    for col in range(0, 11):
        num = row * col
        if num < 10:
            empty = "   "
        elif num < 100:
                empty  = "  "
        else:
            empty = " "

        if col == 0:
            if row == 0:
                print("     ", end="")
            elif row < 10:
                print("   ", row, end="")
            else:
                print("  ", row, end="")
        elif row == 0:
            print("   ", col, end="")
        else:
            print(empty, num, end="")
    print()
