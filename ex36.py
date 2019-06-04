# program reads the letter from the user,
# then determine if the letter is a vovel or a consonant

letter = input("Enter the letter: ")

vovel = ("a", "i", "u", "e", "o")

if letter in vovel:
    print("This letter is a vovel!")
elif letter == "y":
    print("This letter is sometimes a vovel, and sometimes is a consonant.")
else:
    print("This letter is a consonant!")
