
m = int(input("Enter the mass of water (in grams): "))
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

print("Total amount of energy that must be %s to achieve the %s *C temperature is %.2f J" %(temp,t2,q))

# 1J = 1Ws
# 1kWh = 1000W * 3600s

J_in_kWh = 3600000
kWh_zl = 0.6

cost = (q*kWh_zl)/J_in_kWh

print("The cost of heating the water is: %.2f zł" %cost)
