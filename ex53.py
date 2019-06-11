# program reads a rating from the user,
# then reports whether a performance is unacceptable, acceptable or meritorious

rating = float(input("Enter your rating: "))

base = 2400.00

amount = rating*base

if rating == 0.0:
    performance = "unacceptable"
elif rating == 0.4:
    performance = "acceptable"
elif rating >= 0.6:
    performance = "meritorious"
else:
    performance = ""

if performance == "":
    print("Invalid rating was entered.")
else:
    print("Your performance was %s. The amount of your raise is $%s" %(performance,amount))
