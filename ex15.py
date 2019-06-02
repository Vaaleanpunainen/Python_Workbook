# program reads a measurment in feets from user,
# then convert it to inches, yards and mies

feet = float(input("Enter number of feet: "))

inches = feet*12
yards = feet*0.333333
miles = feet*0.000189

print(
"""
%s feet is %s inches, %.2f yards and %s miles
"""
%(feet, inches, yards, miles)
)
