from math import exp

def cosh(x):
    return (exp(x) + exp(-x)) / 2

def sinh(x):
    return (exp(x) - exp(-x)) / 2

def f(a,d,s):
    return a + s - a * cosh(d / (2 * a))

EPSILON = pow(10,-10)
# f(a) = a + s - a * cosh(d / 2a)
# f(a) is strictly monotonic, use binary search over a in (0,10^9]
d,s = map(int,input().split())
L,H = 0,pow(10,9)
while abs(H - L) > EPSILON:
    M = (L + H) / 2
    if f(M,d,s) < 0:
        L = M
    else:
        H = M
print(2 * L * sinh(d / (2 * L)))
