from sys import stdin
from math import gcd

n = int(stdin.readline())
# find gcd of all numbers with 10
# if g = 1, the answer is 1
# else, the answer is n
g = 10
for _ in range(n):
    num = int(stdin.readline())
    g = gcd(num,g)
print(1) if g == 1 else print(n)
