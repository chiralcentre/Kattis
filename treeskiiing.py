from math import factorial

n = int(input())
directions = list(input().split())
freq = {}
for d in directions:
    freq[d] = freq.get(d,0) + 1
print((factorial(n) // (factorial(freq.get("N",0)))) // factorial(freq.get("W",0)) - 1)
