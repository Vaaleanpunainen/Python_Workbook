n = int(input("Enter a number: "))
if n%2 == 1:
    m = 1
    s = n//2
    diamond = ""
    while m < n:
        for i in range(n//2):
            spaces = " " * s
            stars = "*" * m
            m += 2
            s -= 1

            diamond += spaces + stars + "\n"
    diamond += "*" * n + "\n"
    s = 1
    m = n-2
    while m > 0:
        for i in range(n//2):
            spaces = " " * s
            stars = "*" * m
            m -= 2
            s += 1
            diamond += spaces + stars + "\n"

    print(diamond)
else:
    print("Number can not be even!")
