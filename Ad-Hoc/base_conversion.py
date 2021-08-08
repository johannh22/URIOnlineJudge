# -*- coding: utf-8 -*-
# URI 1193: Base Conversion
# 1. Define which is the base of the input (hex, decimal or binary)
# 2. If bin, convert to hex and dec. If dec, convert to hex and bin.
# If hex, convert do dec and bin

def convertBase(n, base):
    if base == 'dec':
        n = int(n)
        h = f'{hex(n)[2:]} hex'
        b = f'{bin(n)[2:]} bin'
        return h, b
    elif base == 'hex':
        n = '0x' + n
        n = int(n, 16)
        d = f'{n} dec'
        b = f'{bin(n)[2:]} bin'
        return d, b
    elif base == 'bin':
        n = '0b' + n
        n = int(n, 2)
        d = f'{n} dec'
        h = f'{hex(n)[2:]} hex'
        return d, h
    else:
        raise ValueError("Base not supported!")

N = int(input()) # number of test cases

for i in range(N):
    numBase = input().split()
    res = convertBase(numBase[0], numBase[1])
    print(f"Case {i+1}:")
    print(f"{res[0]}")
    print(f"{res[1]}\n")