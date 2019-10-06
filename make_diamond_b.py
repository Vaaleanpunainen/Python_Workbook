n = int(input("Enter a number: "))
if n > 0 and n % 2 == 1:
    diamond = ""
    for i in range(n):
        diamond += " " * abs((n//2) - i)
        diamond += "*" * (n - abs((n-1) - 2 * i))
        diamond += "\n"
    print(diamond)
else:
    print("Number can not be even!")
