from sys import stdin

N,W = map(int,stdin.readline().split())
temps = list(map(int,stdin.readline().split()))
best,T,curr,s = -1,W * 60,0,0
for i in range(N):
    t = temps[i]
    while curr + 2 * t > T and s < i:
        curr -= temps[s] * 2
        s += 1
    if curr + 2 * t <= T:
        curr += 2 * t
        best = max(best, i - s + 1)
print(best)

        
            
