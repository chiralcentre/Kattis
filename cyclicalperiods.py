from sys import stdin

N = int(stdin.readline())
longest,ans = -1,""
seen = {}
for i in range(N):
    P,letters = stdin.readline().split()
    P = int(P)
    for L in letters:
        if L in seen:
            period = P - seen[L]
            if period > longest:
                longest,ans = period,L
        seen[L] = P
print(ans)
    
