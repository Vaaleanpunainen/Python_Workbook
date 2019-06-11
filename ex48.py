# program reads a year from the user,
# then displays the animal associated with that year

year = int(input("Enter the year: "))

if year%12 == 0:
    animal = "Monkey"
elif year%12 == 1:
    animal = "Rooster"
elif year%12 == 2:
    animal = "Dog"
elif year%12 == 3:
    animal = "Pig"
elif year%12 == 4:
    animal = "Rat"
elif year%12 == 5:
    animal = "Ox"
elif year%12 == 6:
    animal = "Tiger"
elif year%12 == 7:
    animal = "Here"
elif year%12 == 8:
    animal = "Dragon"
elif year%12 == 9:
    animal = "Snake"
elif year%12 == 10:
    animal = "Horse"
elif year%12 == 11:
    animal = "Sheep"

print("%s is a year of the %s." %(year, animal))
