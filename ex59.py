# program determine whether or not a license plate is valid
# a valid license plate either consist of:
# 1) 3 uppercase letters followed by 3 numbers, or
# 2) 4 numbers followed by 3 uppercase letters

id = input("Enter your licence ID: ")

if id[0:3].isdigit() and id[-3:].isupper():
    style = "newer"
elif id[0:2].isupper() and id[-3:].isdigit():
    style = "older"
else:
    style = ""

if style == "":
    print("The entered ID is not valid for either style of license plate.")
else:
    print("Your ID is valid for %s style license plate." %style)
