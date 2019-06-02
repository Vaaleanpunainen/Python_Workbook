# program asks the user to enter the value of containers,
# then computes and displays the refund for returned containers in $

s_cont = int(input("Enter the number of your small containers (holding one liter or less): "))
l_cont = int(input("Enter the number of your large containers (holding more than one liter): "))

def deposits():
    small = s_cont*0.10
    large = l_cont*0.25
    refund = small + large
    print("The refund of returned containers: $%.2f." %refund)


deposits()
