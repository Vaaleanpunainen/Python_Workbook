# program converts a decimal (base 10) number entered by the user to binary (base 2)

a = int(input("Enter a number (in decimal): "))

# Base 2(binary)
bin_a = bin(a)
print(bin_a)

print("%s in decimal is %s in binary." %(a, bin_a))
