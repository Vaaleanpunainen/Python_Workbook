# program asks the user to enter the amount of MPG,
# then computes and displays amount of L/100 km

am = float(input("Enter the amount of MPG: "))

mi = 1.609
ga = 3.785

ou = (ga * 100) / (am * 1.609)

print("%s mpg US = %.2f L/100km" %(am, ou))
