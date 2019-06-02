# program asks the user to enter the two numbers: a and b,
# then computes and displays:
#
# the sum of a and b
# the difference when b is subtracted from a
# the product of a and b
# the quotient when a is divided by b
# the remainder when a is divided by b
# the result of log10 a
# the result of a^b

from math import log10

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

sm = a + b
print("The sum of %s and %s is %s" %(a, b, sm))

df = a - b
print("The difference when %s is subtracted from %s is %s" %(b, a, df))

pr = a * b
print("The product of %s and %s is %s" %(a, b, pr))

qt = a / b
print("The quotient when %s is divided by %s is %s" %(a, b, qt))

rem = a % b
print("The remainder when %s is divided by %s is %s" %(a, b, rem))

lg = log10(a)
print ("The result of log10(%s) is %s" %(a, lg))

pw = a ** b
print("The power of %s to %s is %s" %(a, b, pw))
