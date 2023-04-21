#!/usr/bin/env python3

import sys

def main():
    number = 1
    s = 'hi'
    print(f'variable number: {number}'); print(type(number)) #print type and var
    print(f'variable S: {s}'); print(type(s)) #print type and var
    a = 2
    b = 3
    if (a > b):
        print('a is greater than b')
    elif (a < b):
        print('a is less than b')
    else:
        print('a and b are equal')
    secMain(1, 10)
    pet = housePet()
    pet.pet()
    pet.sound()



def secMain(c, d):
    d -= 1
    while (c < d):
        c += 1
        print(c)

class housePet:
    p = 'dog'
    o = 'bark'
    def pet(self):
        print(self.p)
    def sound(self):
        print(self.o)


if __name__ == "__main__": main()