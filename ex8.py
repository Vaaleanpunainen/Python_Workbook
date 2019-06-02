# program asks the user to enter the number of widgets and gizmos,
# then computes and displays the total weight of an order

widgets = int(input("Enter the number of widgets: "))
gizmos = int(input("Enter the number of gizmos: "))

def order_weight():
    w1 = widgets*75
    w2 = gizmos*112
    o_w = (w1 + w2)/1000
    print("Your order weight is %s kg" %o_w)

order_weight()
