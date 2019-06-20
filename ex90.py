# program displays if entered string is integer or not

def isInteger(text):
    i = 0
    result = text.replace(" ", "")
    if len(result) > 0:
        if result[:].isdigit():
            return 'is integer.'
        elif (result[0] == "+" or result[0] == "-") and result[1:].isdigit():
            return 'is integer.'
        else:
            return 'is no integer.'
    else:
        return 'is no integer.'

def main():
    text = input("Enter a string: ")
    print("This string", isInteger(text))


#only call the main function when this file has not been imported
if __name__ == "__main__":
    main()
