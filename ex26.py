# program displays the time, when program was created and the current time

import time

t = (2019, 6, 4, 11, 52, 30, 1, 155, 0)
print("Time, when program was created: ", time.asctime(t))

print("Time now: ", time.asctime())

# Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
# When the time tuple is not present, current time as returned by localtime() is used.
