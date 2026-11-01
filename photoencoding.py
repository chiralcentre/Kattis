from sys import stdin
from math import ceil

m = int(stdin.readline())
# number of possible pixels with manhanttan distance of d from top left pixel = d + 1
# range of dimensions of squares for pixels of d distance = [d // 2 + 1, d + 1]
freq = {}
for i in range(m):
    d = int(stdin.readline())
    freq[d] = freq.get(d,0) + 1
ans = -1
for key,value in freq.items():
    L = ceil(key / 2) + 1
    s = 2 if key % 2 else 1
    L += max(0, ceil((value - s) / 2))
    ans = max(ans,L)
print(ans)
