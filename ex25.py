# program reads a duration from the user as a number of seconds,
# then returns the equivalent amount of time in the form D:HH:MM:SS

seconds = int(input("Enter the number of seconds: "))

sec_per_d = 86400
sec_per_h = 3600
sec_per_min = 60

d1 = seconds // sec_per_d
s2 = seconds % sec_per_d

h1 = s2 // sec_per_h
s3 = s2 % sec_per_h

m1 = s3 // sec_per_min
s4 = s3 % sec_per_min

print("The equivaent duration is: %d:%02d:%02d:%02d" %(d1,h1,m1,s4))
