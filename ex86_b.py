# Genere the complete lyrics for song The Twelve Days of Christmas

days = ['first','second','third','forth','fifth', 'sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']

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
        d = (-1 + number)
        print(
"""
On the %s day of Christmas
My true love sent to me:"""
%(days[d]))

        if number == 1:
            print(text[0])
        else:
            for number in text[i:]:
                print(number)

main()
