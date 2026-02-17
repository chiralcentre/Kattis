from sys import stdin

N = int(stdin.readline())
monsters = list(map(int,stdin.readline().split()))
freq = {}
for m in monsters:
    freq[m] = freq.get(m,0) + 1
ans = 0
for k,v in freq.items():
    if v >= k:
        ans += v - k
    else:
        ans += v
print(ans)
