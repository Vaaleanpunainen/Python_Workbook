# Convert a height in feet and inches to meters and centimeters

print("Enter your height:")
feet = float(input("Number of feet: "))
inches = float(input("Number of inches: "))


feet_to_inches = feet*12
centimeters = (feet_to_inches + inches)*2.54
cm_per_m = 100

m = centimeters // cm_per_m
cm = centimeters % cm_per_m

print("Your heigh is %.0f m %.0f cm" %(m,cm))
