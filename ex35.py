# program implements the conversion from human years to dog years

# 1-2 years old +10.5 dogs years per human year
# above 2 years old +4 dogs years per human year

age = int(input("Enter your dog age: "))

if age < 0:
    print("The age can not be negative!")
elif age <= 2:
    output = age * 10.5
    print("The age of your dog in human years is equal %s" %output)
elif age > 2:
    output = 21 + (age-2)*4
    print("The age of your dog in human years is equal %s" %output)
