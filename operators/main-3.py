#!/usr/bin/env python3

x = int(input('first number: '))
y = int(input('second number: '))

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)

if (x > y):
    print('x is greater than y')
elif (x > y):
    print('y is greater than x')
elif (x == y):
    print('they are equal')
else:
    print('false')

n = range(0, 99)
for i in n:
    print('{}'.format(i))

if (x in n and y in n):
    print('both numbers is in list')
elif (x in n or y in n):
    print('one number is in the list')
else:
    print('no numbers are in the list')