#!/usr/bin/python3.8

def fibon(n):
    if n == 1:
        return 1
    elif  n == 2:
        return 1
    else:
        return fibon(n-1) + fibon(n-2)

print(fibon(n))


