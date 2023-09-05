from sys import stdin,stdout
from math import gcd

A,B,C,D = map(int,stdin.readline().split())
LCM = C // gcd(C, D) * D
ans = B // LCM - (A - 1) // LCM
stdout.write(f"{ans}\n")
