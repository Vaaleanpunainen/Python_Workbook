# program is a coin flip simulator

import random

outcome = ['H', 'T']

average = 0
loop = 10

T = 0
H = 0

while loop > 0:
    output = ''
    flips = 0
    loop -= 1
    while True:
        simulation = outcome[random.randint(0,1)]
        output = output + simulation
        T = output.count('TTT')
        H = output.count('HHH')
        flips += 1
        if T == 1 or H == 1:
            average = average + flips
            print("1)", output, "(%s flips)" %flips)
            break

average = average / 10

print("On average, %s flips were needed" %average)

# simulation = random.choice(outcome)
