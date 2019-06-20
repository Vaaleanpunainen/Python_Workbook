# program capitalizes an entered string

def capitalize(text):

    result = text.replace(" i ", " I ")

    if len(text) > 0:
        result = result[0].upper() + result[1:len(result)]

    i = 0
    while i < len(text):
        if result[i] == "." or result[i] == "?" or result[i] == "!":
            i += 1
            while i < len(text) and result[i] == " ":
                i += 1
            if i < len(text):
                result = result[0:i] + result[i].upper() + result[i+1:len(result)]

        i += 1

    return result


def main():
    text = input("Enter a message: ")
    print(capitalize(text))

main()
