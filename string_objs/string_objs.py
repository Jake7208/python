#!/usr/bin/env python3
def main():
    usrIn = input('Input a word: ')
    x = []

    for i in usrIn:
        x.append(i)
        print(i)
    for i in reversed(usrIn):
        print(i)
    newVar = usrIn[::-1]
    print(newVar)

    n = str(input('Give me a letter'))
    print(usrIn.count(n))


if __name__ == '__main__': main()
