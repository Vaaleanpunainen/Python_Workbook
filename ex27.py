# program reads an information about weight and height from user,
# then computes and displays user's BMI and information about weight status


weight = float(input("Enter your weight (in kg): "))
height = (float(input("Enter your height (in cm): ")))/100

BMI = weight/(height*height)

print("Your BMI is %.2f" %BMI)

if BMI < 18.5:
    print("You are underweight!")
elif 18.5 <= BMI < 25.0:
    print("It is normal range.")
elif 25.0 <= BMI < 30.0:
    print("You are overweight!")
elif 30 <= BMI:
    print("It is obese!")
