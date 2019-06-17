# program reads two positive integers from the user
# then determines and report their greatest common dividor

a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a > b:
    d = b
else:
    d = a

while a % d != 0 or b % d != 0:
    d -= 1

print(d)
