# program reads values of triangle sides,
# then displays the triangle's name


a = int(input("Enter value of side a: "))
b = int(input("Enter value of side b: "))
c = int(input("Enter value of side c: "))

if a != b != c:
    name = "Scalene"
elif a == b == c:
    name = "Equilateral"
else:
    name = "Isosceles"

print("%s is type of your triangle." %name)
