from math import factorial

def S(n):
    return factorial(2*n+2)//((factorial(n+1)**2)*(n+2))

print(S(int(input())))
