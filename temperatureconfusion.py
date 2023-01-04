from math import gcd

a,b = map(int,input().split('/'))
a -= 32 * b
a *= 5; b *= 9
d = gcd(a,b)
a //= d; b //= d
print(f"{a}/{b}") if a >= 0 else print(f"-{abs(a)}/{b}")
