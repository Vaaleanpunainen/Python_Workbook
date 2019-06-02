# program asks the user to enter the positive number, n,
# then displays the sum of all of the integers from 0 to n

number = int(input("Enter the positive number: "))


def sum_n():
    sm = int(number*(number+1)/2)
    print("The sum of the first", number, "positive integers is %s" %sm)

sum_n()
