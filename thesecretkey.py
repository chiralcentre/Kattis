from sys import stdin

N = int(stdin.readline())
used = set()
for _ in range(N):
    s = stdin.readline().strip()
    k = int(s, 2)
    used.add(k)
s = 0
while s in used:
    s += 1
print(bin(s)[2:].zfill(N))
