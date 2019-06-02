water_heat_capacity = 4.186
electricyty_price = 60
j_to_kwh = 2.777e-7

volume = float(input("Enter the amount of water in milliliters: "))
d_temp =float(input("Enter the temperature increase (degrees Celsius): "))

q = volume * d_temp * water_heat_capacity

print("That will require %d J of energy" %q)

kwh = q * j_to_kwh
cost = kwh * electricyty_price

print("That much energy will cost %.2f groszy." %cost)
