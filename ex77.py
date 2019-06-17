num = input("Enter a number (in binary): ")

i = len(num) - 1

dec = 0

while i >= 0:
    for n in num:
        x = int(n)*(2**i)
        dec = dec + x
        i -= 1

print("%s in binary is %s in decimal." %(num, dec))
