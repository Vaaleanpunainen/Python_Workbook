# random lottery numbers

import random
lottery = []

while len(lottery) < 7:
    number = int(random.randint(1,49))
    if number not in lottery:
        lottery.append(number)
lottery.sort()
print(lottery)
