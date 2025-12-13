from math import lcm

d1,d2,d3 = map(int,input().split())
n = int(input().strip())

A = lcm(d1,d2,d3)
F = 0
# calculate number of free days in each cycle of A days
# can be done by brute force since d1 * d2 * d3 is maximum 125000
for i in range(1, A + 1):
    if i % d1 and i % d2 and i % d3:
        F += 1
T = (n // F) * A
P = (n // F) * F
if P == n:
    T -= A
    P -= F
while P < n:
    T += 1
    if T % d1 and T % d2 and T % d3:
        P += 1
print(T)
