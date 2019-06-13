# program reads the temperature from the user in degrees Celsius,
# then computes and displays the equivalent temperature in degrees
# Fahrenheit and degrees Kelvin

t = float(input("Enter the temperature (in degrees Celsius): "))

if t < -273.15:
    print("This temperature doesn't exist!")
else:
    f = t * 9/5 + 32
    k = t + 273.15
    print("This temperature is equal to %.2f degrees Fahrenheit and %s degrees Kelvin." %(f,k))
