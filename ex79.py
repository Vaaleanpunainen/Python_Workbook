# program selects a random integer between 1 and 100,
# and saves this integer as a maximum value,
# then selects a random 99 integers and check each integer
# as it is larger than the maximum value encountered so far
# if it is then program update the maximum number and count the fact

import random

max_number = int(random.randint(0,100))
print(max_number, "<== FIRST MAX")

updates = 0

for x in range(99):
    next_number = int(random.randint(1,100))
    if max_number > next_number:
        print(next_number)
    else:
        print(next_number, "<== UPDATE")
        max_number = next_number
        updates += 1

print("The maximum value found was %s." %max_number)
print("The maximum value was updated %s times." %updates)
