# avoiding duplicates

words = []
word = input("Enter a word (blank to exit): ")
while word != "":
    if word not in words:
        words.append(word)
    word = input("Enter a word (blank to exit): ")

print("Your inputs without duplicates: ")
for w in words:
    print(w)
