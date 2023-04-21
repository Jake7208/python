#!/usr/bin/env python3

def main():
    fruit = [ 'Apples', 'Pears', 'Oranges', 'Peaches' ]
    print(fruit)
    fruit.append(input('Add new fruit : '))
    print_list(fruit)
    u = int(input('Enter a number : '))
    print(fruit[u], u)
    fruit.insert(0, 'strawberry')
    print(fruit)
    print_list(fruit)
    about = dict(name = 'Chris', city = 'Seattle', cake = 'Chocolate')
    print(about)
    about.pop('cake')
    print(about)
    about['fruit'] = 'mango'
    print(about)
    print(about.keys())
    print(about.values())
    if ('cake' in about.keys()):
        print('true')
    else:
        print('false cake is not a key')

    for key in about.keys():
        print(key)

    if ('mango' in about.values()):
        print('true mango is in values')
    else:
        print('false')
    s2 = set(range(0, 21, 2))
    s3 = set(range(0, 21, 3))
    s4 = set(range(0, 21, 4))
    print(s2)
    print(s3)
    print(s4)
    print(s2 | s3)
    print(s3 & s4)
def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()


if __name__ == '__main__': main()