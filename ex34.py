# program reads an integer from the user,
# then displays a message indicating whether integer is even or odd


number = int(input("Enter the number: "))

if number % 2 == 0:
    print("This number is even!")
else:
    print("This number is odd!")
