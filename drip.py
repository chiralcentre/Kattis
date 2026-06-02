from sys import stdin

s,m,n = map(int,stdin.readline().split())
for _ in range(n):
    line = stdin.readline().split()
    if line[0] == "DRIP":
        d,p = int(line[1]),int(line[2])
        T = d * s
        s += T // p
        m += T % p
    else:
        p = int(line[1])
        s += m // p
        m %= p
print(s)
print(m)
