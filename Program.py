import random

def generator(numchar):

    name = "Password: "
    char = ""
    while numchar > -1:
        x = random.randrange(0,25)
        name = str(name) + str(char)
        if x == 0:
            char = "a"
            numchar = numchar - 1
        if x == 1:
            char = "b"
            numchar = numchar - 1
        if x == 2:
            char = "c"
            numchar = numchar - 1
        if x == 3:
            char = "d"
            numchar = numchar - 1
        if x == 4:
            char = "e"
            numchar = numchar - 1
        if x == 5:
            char = "f"
            numchar = numchar - 1
        if x == 6:
            char = "g"
            numchar = numchar - 1
        if x == 7:
            char = "h"
            numchar = numchar - 1
        if x == 8:
            char = "i"
            numchar = numchar - 1
        if x == 9:
            char = "j"
            numchar = numchar - 1
        if x == 10:
            char = "k"
            numchar = numchar - 1
        if x == 11:
            char = "l"
            numchar = numchar - 1
        if x == 12:
            char = "m"
            numchar = numchar - 1
        if x == 13:
            char = "n"
            numchar = numchar - 1
        if x == 14:
            char = "o"
            numchar = numchar - 1
        if x == 15:
            char = "p"
            numchar = numchar - 1
        if x == 16:
            char = "q"
            numchar = numchar - 1
        if x == 17:
            char = "r"
            numchar = numchar - 1
        if x == 18:
            char = "s"
            numchar = numchar - 1
        if x == 19:
            char = "t"
            numchar = numchar - 1
        if x == 20:
            char = "u"
            numchar = numchar - 1
        if x == 21:
            char = "v"
            numchar = numchar - 1
        if x == 22:
            char = "w"
            numchar = numchar - 1
        if x == 23:
            char = "x"
            numchar = numchar - 1
        if x == 24:
            char = "y"
            numchar = numchar - 1
        if x == 25:
            char = "z"
            numchar = numchar - 1
        while numchar == -1:
            print(name)
            generator(int(input("How many characters? ")))     

generator(int(input("How many characters? ")))