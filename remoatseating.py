from sys import stdin
from math import factorial,gcd

N = int(stdin.readline())
teams = map(int,stdin.readline().split())
numerator,T = 1,0
for t in teams:
    numerator *= factorial(t)
    T += t
numerator *= factorial(N)
denominator = factorial(T)
D = gcd(numerator, denominator)
print(f"{numerator // D}/{denominator // D}")
