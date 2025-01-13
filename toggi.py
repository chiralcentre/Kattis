from math import log10

def compute_num(m):
    return m * log10(m)

C = int(input())
C *= pow(10,6)
# perform binary search on answer, find largest value of C such that n log n <= C * 10^6
s,e,ans = 1,pow(10,18),-1
while s <= e:
    m = (s + e) >> 1
    res = compute_num(m)
    if res <= C:
        s = m + 1
        ans = m
    else:
        e = m - 1
print(ans)
