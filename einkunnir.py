from sys import stdin,stdout

S,N = map(int,stdin.readline().split())
ans = stdin.readline().split()
for i in range(N):
    name = stdin.readline().strip()
    sub = stdin.readline().split()
    correct = sum(ans[j] == sub[j] for j in range(S))
    numerator = correct * 10
    rem = numerator % S
    d = -1
    if rem * 4 < S:
        d = 0
    elif rem * 2 <= S or 4 * rem < 3 * S:
        d = 5
    else:
        d = 0
        numerator += S
    stdout.write(f"{name}: {numerator // S}.{d}\n")
