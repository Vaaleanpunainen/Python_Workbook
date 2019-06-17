# program converts a decimal (base 10) number entered by the user to binary (base 2)

decimal = int(input("Enter a number (in decimal): "))

result = ""

q = decimal

if q == 0:
    result = 0
else:
    while q > 0:
        r = q % 2
        result = str(r) + result
        q = q // 2

print("%s in decimal is %s in binary." %(decimal, result))
