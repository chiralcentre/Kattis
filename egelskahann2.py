from math import log2,floor

# Josephus problem: https://en.wikipedia.org/wiki/Josephus_problem
n = int(input())
print(2 * (n - pow(2, floor(log2(n)))) + 1)
