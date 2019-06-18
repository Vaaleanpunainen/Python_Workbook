# program converts and integer to its ordinal number

def convert(number):
    if number == 1:
        return 'first'
    elif number == 2:
        return 'second'
    elif number == 3:
        return 'third'
    elif number == 4:
        return 'forth'
    elif number == 5:
        return 'fifth'
    elif number == 6:
        return 'sixth'
    elif number == 7:
        return 'seventh'
    elif number == 8:
        return 'eighth'
    elif number == 9:
        return 'ninth'
    elif number == 10:
        return 'tenth'
    elif number == 11:
        return 'eleventh'
    elif number == 12:
        return 'twelfth'
    else:
        return ''

def main():
    for number in range(1,13):
        print(number, convert(number))

main()
