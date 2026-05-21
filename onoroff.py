from sys import stdin
from math import comb

# for each test case, divide the N + M batteries in N - 1 groups as evenly as possible
# by Pigeonhole principle, one of this group is bound to have 2 healthy batteries
# try every pair of batteries within each group
for _ in range(int(stdin.readline())):
    N,M = map(int,stdin.readline().split())
    T = N + M
    P,E = T //(N - 1),T % (N - 1)
    # E groups have size P + 1
    # (N - 1 - E) groups have size P
    print(E * comb(P + 1, 2) + (N - 1 - E) * comb(P, 2))
