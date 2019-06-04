# program reads the name of a month from the user as a string,
# then sisplays the number of days in that month

mon = input("Enter the name of the month: ")

thirty = ("April", "June", "September", "November")
thirty_one = ("January", "March", "May", "July", "August", "October", "December")
twenty_eight = ("February")

if mon in thirty:
    number = "30"
elif mon in thirty_one:
    number = "31"
elif mon in twenty_eight:
    number = "28 or 29"
else:
    number = ""

if number == "":
    print("Wrong name of the month! Please double check it.")
else:
    print("The number of days in %s is equal %s." %(mon, number))
