# program reads the current date from the user,
# then displays next day date

year = int(input("Enter the year (YYYY): "))
month = int(input("Enter the month (MM): "))
day = int(input("Enter the day (DD): "))

days_30 = (4, 6, 9, 11)
days_31 = (1, 3, 5, 7, 8, 10, 12)

if year % 400 == 0:
    isLeapYear = True
elif year % 4 == 0 and year % 100 != 0:
    isLeapYear = True
else:
    isLeapYear = False

if month in days_30:
    if day < 30:
        day += 1
    else:
        day = 1
        month += 1
elif month in days_31:
    if month == 12 and day >= 31:
        day = 1
        month = 1
        year += 1
    elif day < 31:
        day += 1
    else:
        day = 1
        month += 1
elif month == 2:
    if day < 28:
        day += 1
    else:
        if isLeapYear == True:
            if day == 28:
                day += 1
            else:
                day = 1
                month += 1
        else:
            day = 1
            month += 1

print("The next day is %s %s %s" %(year, month, day))
