# program reads the number of loaves of day old bread being purchased from the user,
# thrn displays the regular price, the discount, and total price

loaves = int(input("Enter the number of loaves of day old bread: "))

normal_p = loaves*3.49
discount_p = loaves*0.6
total_p = normal_p - discount_p

print(
"""
Regular price: $%5.2f
Discount:      $%5.2f
Total price:   $%5.2f
"""
%(normal_p, discount_p, total_p)
)
