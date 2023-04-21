#!/usr/bin/env python3

n = int(input('Enter a number: '))
result = 0

for o in range(n):
    if o % 2 == 0:
       continue
    else:
        print(o)
        result += o
    o+= 1

print(result)