# program comupues the average of a collection of values entered by the user
# when the user enters 0 no further values will be provided

flag = True
sm = 0
av = 0

while flag:
    try:
        n = int(input("Enter a number: "))
        if n == 0:
            flag = False
        else:
            sm += n
            av += 1
    except ValueError:
        print("Entered value is not a number!")
try:
    print(sm/av)
except ZeroDivisionError:
    print("First number can not be 0!")
