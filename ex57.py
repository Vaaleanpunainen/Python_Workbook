# program determines whether or not a year is a leap year

year = int(input("Enter a year: "))

if year % 400 == 0:
    name = "leap"
elif year % 4 == 0 and year % 100 != 0:
    name = "leap"
else:
    name = "not leap"

print("The %s is %s year." %(year, name))
