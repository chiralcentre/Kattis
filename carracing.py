from sys import stdin

n = int(stdin.readline())
total,freq = [0 for _ in range(6)],[0 for _ in range(6)]
for _ in range(n):
    c,p = map(int,stdin.readline().split())
    total[c] += p
    freq[c] += 1
ans,best = None,pow(10,9)
for i in range(1,6):
    if freq[i] != 0:
        average = total[i] // freq[i]
        if average < best:
            ans,best = i, average
print(ans)
print(best)
