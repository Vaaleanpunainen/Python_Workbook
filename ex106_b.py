# remove outliners

def removeOutliners(data):
    list = sorted(data)
    for i in range(2):
        list.pop()
        list.pop(0)
    return list

def main():
    list = []
    l = input("Enter a value (press enter to exit): ")
    while l != "":
        l = float(l)
        list.append(l)
        l = input("Enter a value (press enter to exit): ")

    if len(list) < 4:
        print("Your list can not be less than 4 values!")
    else:
        print("With removed outlines: ", removeOutliners(list))
        print("Orginal values: ", list)


if __name__ == "__main__":
    main()
