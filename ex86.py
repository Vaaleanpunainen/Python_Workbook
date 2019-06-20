# Genere the complete lyrics for song The Twelve Days of Christmas

def days(number):
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

text = ['A partridge in a pear tree.',
'Twelve drummers drumming,',
'Eleven pipers piping,',
'Ten lords a-leaping,',
'Nine ladies dancing,',
'Eight maids a-milking,',
'Seven swans a-swimming,',
'Six geese a-laying,',
'Five golden rings,',
'Four calling birds,',
'Three French hens,',
'Two turtle doves,',
'And a partridge in a pear tree!']


def main():
    for number in range(1,13):
        i = -(0+number)
        if number == 1:
            print(
"""
On the %s day of Christmas
My true love sent to me:"""
%(days(number))
                )
            print(text[0])

        else:
            print(
"""
On the %s day of Christmas
My true love sent to me:"""
%(days(number))
                )

            for number in text[i:]:
                print(number)

main()
