from math import gcd
# refer to https://cs.baylor.edu/~hamerly/icpc/qualifier_2019/outlines-naq-2019.pdf for explanation
M,N = map(int,input().split()) #M = number of rows, N = number of columns
D = gcd(N,M); N //= D; M //= D;
print(D) if N%2 and M%2 else print(0)
