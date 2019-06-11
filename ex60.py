# program simulates a spin of a roulette wheel

import random

result = (random.randint(0,37))

white = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)


if result == 37:
    print("The spin result in 00...")
else:
    print("The spin result in %s..." %result)

if result == 37:
    print("Pay 00")
else:
    print("Pay %s" %result)

if result == 0 or result == 37:
    print("Pay Green")
elif result in white:
    print("Pay White")
else:
    print("Pay Black")

if 1 <= result <= 36:
    if result % 2 == 0:
        print("Pay Even")
    else:
        print("Pay Odd")

if 1 <= result <= 18:
    print("Pay 1 to 18")
elif 19 <= result <= 36:
    print("Pay 19 to 36")
