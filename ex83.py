# program reads a number of items in the order from the user


def express_shipping(x):
    if x == 1:
        charge = 10.95
    else:
        charge = 10.95 + 2.95*(x-1)
    return charge

def main():
    x = int(input("Enter the number of items: "))
    print("Your shipping charge is: $%.2f" %express_shipping(x))

main()
