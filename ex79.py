import random

max_number = int(random.randint(0,100))
print(max_number, "<== FIRST MAX")

updates = 0

for x in range(99):
    number = random.randint(1,100)
    next_number = int(number)
    if max_number > next_number:
        print(next_number)
    else:
        print(next_number, "<== UPDATE")
        max_number = next_number
        updates += 1

print("The maximum value found was %s." %max_number)
print("The maximum value was updated %s times." %updates)
