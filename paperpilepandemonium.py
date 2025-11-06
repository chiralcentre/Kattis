from sys import stdin,stdout

N,P = map(int,stdin.readline().split())
piles = [[] for _ in range(P)]
for i in range(P):
    _,*nums = map(int,stdin.readline().split())
    piles[i] = nums
for j in range(int(stdin.readline())):
    s,d,n = map(int,stdin.readline().split())
    s -= 1; d -= 1
    for k in range(n):
        piles[d].append(piles[s][-n + k])
    for _ in range(n):
        piles[s].pop()
for pile in piles:
    stdout.write(" ".join(str(num) for num in pile))
    stdout.write("\n")
