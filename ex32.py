# program reads 3 integers from the user
# and displays them in sorted order (from smallest to largest)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

min_num = min(n1, n2, n3)
max_num = max(n1, n2, n3)
med_num = n1 + n2 + n3 - min_num - max_num

print(
"""
The smallest one is number %s
The largest one is number %s
The medium number is %s
"""
%(min_num, max_num, med_num)
)
