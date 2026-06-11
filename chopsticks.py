from sys import stdin

n,m = map(int,stdin.readline().split())
freq = {}
for _ in range(m):
    x1,x2 = map(int,stdin.readline().split())
    freq[(x1,x2)] = freq.get((x1,x2),0) + 1
pairs = sum(val // 2 for _,val in freq.items())
print("yes") if pairs >= n else print("no")
