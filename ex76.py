# program reads a number entered by the user,
# then displays a prime factors

num = int(input("Enter a number (greather than 1): "))

n = num

factor = 2


if n < 2:
    print("Error.")
else:
    print("The prime factors of %s are:" %(num))
    while factor <= n:
        if n % factor == 0:
            n_factor = factor
            n = n / n_factor
            print(n_factor)
        else:
            factor +=1
