# program asks the user to enter the width and lenght of their room,
# then computes and displays the area of the room

width = float(input("Enter the width of your room (in meters): "))
lenght = float(input("Enter the lenght of your room (in meters): "))

def room_area():
    area = width*lenght
    print("Your room is %s-meter square." %area)

room_area()
