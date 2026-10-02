from sys import stdin

EPSILON = pow(10,-8)

a,d = map(int,stdin.readline().split())
ascent,descent = [],[]
at,dt,ae,de = 0,0,0,0
for _ in range(a):
    h,t = map(int,stdin.readline().split())
    ascent.append((h,t))
    at += t
    ae += h
for _ in range(d):
    h,t = map(int,stdin.readline().split())
    descent.append((h,t))
    dt += t
    de += h
assert ae == de

# H is at most 500000
L,H = 0,min(at,dt)
# binary search on time range
# code runs in O(a + d), since 100 is a constant
for _ in range(100):
    M = (L + H) / 2
    A,ac = 0,0
    for h,t in ascent:
        if ac + t > M:
            r = M - ac
            A += (r / t) * h
            break
        else:
            ac += t
            A += h
    D,dc = 0,0
    for h,t in descent:
        if dc + t > M:
            r = M - dc
            D += (r / t) * h
            break
        else:
            dc += t
            D += h
    if A + D >= ae:
        H = M
    else:
        L = M
print(H)
