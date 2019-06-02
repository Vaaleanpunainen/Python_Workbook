# program asks the user to enter the amount of deposited money,
# then computes and displays the amount in the savings account after 1, 2 and 3 years


deposit = float(input("Enter the amount of deposited money: "))

def savings_amount():
    s1 = deposit + deposit*0.04
    s2 = s1 + s1*0.04
    s3 = s2 + s2*0.04

    print(
    """
    Your amount in the saving account after:
    1 year: $%.2f
    2 years: $%.2f
    3 years: $%.2f
    """
    %(s1, s2, s3)
    )

savings_amount()
