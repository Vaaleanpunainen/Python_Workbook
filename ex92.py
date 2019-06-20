# programs displays whether or not an entered integer is prime number

def prime(n):
    if n <= 1:
        return False

    for x in range(2,n):
        if n % x == 0:
            return False
    return True

def main():
    n = int(input("Enter a number: "))
    if prime(n):
        print("It is a prime number.")
    else:
        print("It isn't a prime number.")

if __name__ == "__main__":
    main()
