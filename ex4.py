# program asks the user to enter the width and lenght of their field,
# then computes and displays the area of the field in acres

width = float(input("Enter the width of your field (in feet): "))
lenght = float(input("Enter the lenght of your field (in feet): "))

def field_area():
    area = (width*lenght)/43560
    print("Your field has %s acre." %area)

field_area()
