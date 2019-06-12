# program shows a discount table 

old = [4.95, 9.95, 14.95, 19.95, 24.95]

print("Old price:  Discount:   New price:")

for n in old:
    print(("$%5.2f      $%5.2f      $%5.2f") %(n, n*0.4, n*0.6))
