# program reads a four-digit integer from the user
# and displays the sum of the digits in the number

# 1234
# 1 + 2 + 3 + 4 = 10

number = int(input("Enter the number: "))

def sum_digits(num):
    return sum([int(n) for n in list(str(num))])

print(sum_digits(number))
