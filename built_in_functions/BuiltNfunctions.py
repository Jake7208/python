#!/usr/bin/env python3



def main():

    # function 1 the ( all() built in function)
    try:
        x = int(input("Enter a number: "))
        y = [x, 3, 3]
        z = all(y)
        print(z)
    except ValueError:
        print("there was a Value Error:", ValueError )

    #function 2 the ( eval() built in function)
    try:
        d = 'print("Hello it\'s valid")'
        eval(d)
    except SyntaxError:
        print("SyntaxError: ", SyntaxError)

    #function 3 the ( hex() function)

    try:
        usrNum = int(input('Insert a number: '))
        x = hex(usrNum)
        print('Inserted number as a hexidecimal :', x)
    except ValueError:
        print('there was a Value Error:', ValueError)

if __name__ == "__main__" : main()