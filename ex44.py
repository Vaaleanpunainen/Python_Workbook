# proggram reads a date from the user,
# then displays a message if entered date correspond to a holiday or not

month_and_day = input("Enter the date (MM/DD): ")

if month_and_day == "01/01":
    name = "New Year's day"
elif month_and_day == "07/01":
    name = "Canada day"
elif month_and_day == "12/25":
    name = "Christmas day"
else:
    name = ""

if name == "":
    print("Entered month and day do not correspond to a fixed-date hoiday.")
else:
    print("%s is a %s." %(month_and_day, name))
