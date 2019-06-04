# program reads the mass of some water and the temperature change from user,
# then displays the total amount of energy that must be added or removed to achieve
# the desired temperature change and computes the cost of heating the water (in groszy)


m = int(input("Enter the amount of water (in milliliters): "))
t1 = float(input("Enter the initial temperature: "))
t2 = float(input("Enter the target temperature: "))

if t1 <= t2:
    dt = t2-t1
    temp = "added"
elif t2 <= t1:
    dt = t1 - t2
    temp = "removed"

C = 4.186

q = m*C*dt

print("Total amount of energy that must be %s to achieve the temperature of %s Celsius degrees is %.2f J" %(temp,t2,q))

# 1J = 1Ws
# 1kWh = 1000W * 3600s

J_in_kWh = 3600000
kWh_zl = 60

cost = (q*kWh_zl)/J_in_kWh

if t1 <= t2:
    print("The cost of heating the water is %.2f groszy." %cost)
elif t2 <= t1:
    print("No costs.")
