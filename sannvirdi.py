from sys import stdin,stdout
from bisect import bisect_left

# binary search for each query
# total time complexity = O(n log n + q log n)
n = int(stdin.readline())
g,p = [],{}
for _ in range(n):
    name,a = stdin.readline().split()
    a = int(a)
    g.append(a)
    p[a] = name
g.sort()

for i in range(int(stdin.readline())):
    d = int(stdin.readline())
    if d in p:
        stdout.write(f"{p[d]}\n")
    else:
        j = bisect_left(g,d)
        stdout.write(":(\n") if j == 0 else stdout.write(f"{p[g[j - 1]]}\n")
