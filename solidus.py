from math import gcd

n = int(input())
input()
d = int(input())
if d < 0:
    n,d = -n,-d
m = gcd(n,d)
if n % d:
    print(f"{n//m}/{d//m}")
else:
    print(n // d)

