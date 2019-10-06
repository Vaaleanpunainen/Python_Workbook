# formatting a list

item = input("Add an item (press enter to exit): ")
list = []
while item != "":
    list.append(item)
    item = input("Add an item (press enter to exit): ")

if len(list) <= 1:
    output_str = ''.join(list)
elif len(list) == 2:
    output_str = ' and '.join(list)
elif len(list) > 2:
    output_str = ', '.join(list[:-1])
    output_str = output_str + ' and ' +list[len(list)-1]


print(output_str)
