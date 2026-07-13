from sys import stdin
from math import log2

# always drink largest drink first
# when caffeine has decayed to x, drink another
# a * (1 / 2) ^ h = x -> a = x  * 2 ^ h -> log2(a / x) = h
n,x = map(int,stdin.readline().split())
drinks = sorted([int(stdin.readline()) for _ in range(n)], reverse = True)
T = log2(drinks[0] / x)
for i in range(1, n):
    T += log2(1 + drinks[i] / x)
print(T)
