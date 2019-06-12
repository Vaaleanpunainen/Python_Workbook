# program computes the total due when several items are purchased
# the amount payable for cash is rounded to the closest nickel
# because pennies have been phased out in Canada

flag = True
sm = 0.00
pennies_per_nickel = 5
nickel = 0.05

while flag:
    n = input("Enter the price of the item (blank to quit): ")
    if n == "":
        flag = False
    else:
        sm += float(n)

round = sm * 100 % pennies_per_nickel

if round < pennies_per_nickel / 2:
    total = sm - round / 100
else:
    total = sm + nickel - round / 100


print("The exact amount payable: $%.02f" %sm)
print("The amount payable with cash: $%.02f" %total)
