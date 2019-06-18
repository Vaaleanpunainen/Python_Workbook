# program reads a distance from the user,
# then computes and displays a total fare fir taxi drive

distance = int(input("Enter a distance (in km): "))

base = 4
travel = 0.25

def total_fare():
    fare = base + distance*travel
    return fare

print(total_fare())
