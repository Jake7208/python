#!/usr/bin/env python3
import logging
import os

def main():
    with open('p1.txt') as f1, open('p2.txt') as f2:
        outfile = open('p1n2-copy.txt', 'wt')
        print(f1.read(), f2.read())
        for i in range(47):
            print(f1.readline().rstrip(), file=outfile)
            print(f2.readline().rstrip(), file=outfile)
            print('.', end='', flush=True)
        outfile.close()
        print('\ndone')


if __name__ == '__main__' : main()

