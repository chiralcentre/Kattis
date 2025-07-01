from sys import stdin
from math import gcd

x,n = input().split()
n = int(n)
a,b = x.split(".") # split into integer and decimal parts
# to get to repeating part, multiply x by 10^(len(b) - n)
# let m = 10^(len(b) - n)
# let m2 = 10^(len(b))
# let c be integer part of x * m
# let d be integer part of x * m2
# x = (d - c) / (m2 - m)
r = b[len(b) - n:]
w = a + b[:len(b) - n]
c = int(w)
d = int(w + r)
num = d - c
denom = pow(10, len(b)) - pow(10,len(b) - n)
D = gcd(num, denom)
print(f"{num // D}/{denom // D}")
