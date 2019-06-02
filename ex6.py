# program asks the user to enter the value of meal and drinks,
# then computes and displays the tax, tip and total amount of the order in $

meal = float(input("Enter the value of your meal (in $): "))
drinks = float(input("Enter the value of your drinks (in $): "))

def tax_and_tip():
    tax = (meal*8.0)/100 + (drinks*23.0)/100
    tip = ((meal+drinks-tax)*18.0)/100
    grand = meal+drinks+tax+tip

    print(
    """
    Tax: $%.2f
    Tip: $%.2f
    Total: $%.2f
    """
    %(tax, tip, grand)
    )

tax_and_tip()
