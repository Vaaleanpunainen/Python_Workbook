# program reads a three values from the user,
# then compute and sisplays the median value of the entered numbers

def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    print("The median value is %s" %median_value(a,b,c))


def median_value(a,b,c):
    if a > b > c or c > b > a:
        return b
    if a > c > b or b > c > a:
        return c
    if b > a > c or c > a > b:
        return a

# def median_value(a.b,c):
#   return a + b + c - min(a,b,c) - max(a,b,c)

main()
