# program reads the air temperature and wind speed from the user,
# then computes and displays the wind chill index rounded to the closest unteger

Ta = float(input("Enter the temperature (in Celsius degrees): "))
V = float(input("Enter the wind speed (in km/h): "))

WCI = 13.12 + (0.6215*Ta) - 11.37*(V**0.16) + 0.3965*Ta*(V**0.16)

print("The wind chill index is ", round(WCI))
