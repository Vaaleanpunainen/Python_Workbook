# program reads the frequency of the radiation from the user,
# then reports its name

frequency = int(input("Enther the frequency of the radiation: "))

if frequency < 3e9:
    name = "radio waves"
elif 3e9 <= frequency < 3e12:
    name = "microwaves"
elif 3e12 <= frequency < 4.3e14:
    name = "infrared light"
elif 4.3e14 <= frequency < 7.5e14:
    name = "visible light"
elif 7.5e14 <= frequency < 3e17:
    name = "ultraviolet light"
elif 3e17 <= frequency < 3e19:
    name = "x-rays"
else:
    name = "gamma rays"

print("The frequency %s Hz is %s." %(frequency, name))
