# reaching 0 from b means for some integer S, we have b + k * S is a multiple of n -> b + k * S = d * N for some d
# clearly gcd(n,k) divides k * S and d * N so it must divide b
# Bezout's identity: there are integers A,B such that A*n + B*k = gcd(n,k)
from math import gcd

n,b,k = map(int,input().split())
print("YES") if not b % gcd(n,k) else print("NO")
