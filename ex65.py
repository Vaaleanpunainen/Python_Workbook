# program computes the perimeter of a polygon
# the user will enter the blank line for x-coordinate to indicate
# that all of the points been entered

from math import sqrt

perimeter = 0

x1 = float(input("Enter the x part of coordinate: "))
y1 = float(input("Enter the y part of coordinate: "))

prev_x = x1
prev_y = y1

blank = input("Enter the price of the item (blank to quit): ")

while blank != "":
    x2 = float(blank)
    y2 = float(input("Enter the y part of coordinate: "))

    dist = sqrt((prev_x - x2) ** 2 + (prev_y - y2) ** 2)
    perimeter += dist

    prev_x = x2
    prev_y = y2

    blank = input("Enter the price of the item (blank to quit): ")

dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
perimeter += dist

print("The perimeter of that polygon is", perimeter)
