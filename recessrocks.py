from sys import stdin

N = int(stdin.readline())
rocks = list(map(int,stdin.readline().split()))
freq = {}
for r in rocks:
    freq[r] = freq.get(r,0) + 1
print(sum(v - 1 for _,v in freq.items()))
