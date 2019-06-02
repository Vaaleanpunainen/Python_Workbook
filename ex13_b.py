# program reads a number of groszy from the user,
# then computes and displays the denominations of the coins
# that should be used to give that amount of change to the shopper

zl5 = 500
zl2 = 200
zl1 = 100
gr50 = 50
gr20 = 20
gr10 = 10
gr5 = 5
gr2 = 2

coins = int(input("Enter the number of groszy: "))

print(" ", coins // zl5, "of 5 zł")
coins = coins % zl5

print(" ", coins // zl2, "of 2 zł")
coins = coins % zl2

print(" ", coins // zl1, "of 1 zł")
coins = coins % zl1

print(" ", coins // gr50, "of 50 gr")
coins = coins % gr50

print(" ", coins // gr20, "of 20 gr")
coins = coins % gr20

print(" ", coins // gr10, "of 10 gr")
coins = coins % gr10

print(" ", coins // gr5, "of 5 gr")
coins = coins % gr5

print(" ", coins // gr2, "of 2 gr")
coins = coins % gr2

print(" ", coins, "of 1 gr")
