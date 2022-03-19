from sys import stdin,stdout
from itertools import permutations

def equation(x,y,z):
        if x + y == z:
            return f'{x}+{y}={z}'
        elif x == y + z:
            return f'{x}={y}+{z}'
        elif x == y - z: # no x - y = z case since x - y = z => x = y + z
            return f'{x}={y}-{z}'
        elif x * y == z:
            return f'{x}*{y}={z}'
        elif x == y * z:
            return f'{x}={y}*{z}'
        else: # last case is x == y//z
            return f'{x}={y}/{z}'
        
a,b,c = map(int,stdin.readline().split())
stdout.write(f'{equation(a,b,c)}\n')
