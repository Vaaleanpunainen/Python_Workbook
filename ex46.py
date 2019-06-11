# program reads a month and day from the user,
# then displays the season associated with the date

month = input("Enter the name of the month: ")
day = int(input("Enter the day number: "))

spring = ("April", "May")
summer = ("July", "August")
fall = ("October", "November")
winter = ("January", "February")


if month in spring:
    name = "spring"
elif month in summer:
    name = "summer"
elif month in fall:
    name = "fall"
elif month in winter:
    name = "winter"
elif month == "March":
    if day >= 20:
        name = "spring"
    else:
        name = "winter"
elif month == "June":
    if day >= 21:
        name = "summer"
    else:
        name = "spring"
elif month == "September":
    if day >= 22:
        name = "fall"
    else:
        name = "summer"
elif month == "December":
    if day >= 21:
        name = "winter"
    else:
        name = "fall"

print("%s %s is in %s." %(month, day, name))
