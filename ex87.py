# program centers a given string in the terminal

import shutil
columns, rows = shutil.get_terminal_size(fallback=(80, 24))

w = columns
# or with a given width i.e.: w = 100

def str_center(s,w):
    spaces = (w - len(s)) // 2
    new_string = " "*spaces + s
    return new_string

def main():
    s = input("Enter a string: ")
    print(str_center(s,w))

main()
