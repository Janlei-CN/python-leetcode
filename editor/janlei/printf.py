#!/bin/python3
import sys


def prinf(x, y, z, n):
    print('[',end='')
    for a in range(x + 1):
        for b in range(y + 1):
            for c in range(z + 1):
                if a + b + c != n:
                    print([a,b,c],end='')
                    if not (a == x and c == z):
                        print(',',end='')
    print(']',end='')

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    prinf(x, y, z, n)

