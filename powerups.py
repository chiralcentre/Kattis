from math import factorial

n,k = map(int,input().split())
T = n + k - 1
print(factorial(T) // (factorial(n - 1) * factorial(T - n + 1)))
