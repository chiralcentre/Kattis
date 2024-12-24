from sys import stdin,stdout

n = int(stdin.readline())
events = []
for i in range(n):
    e,s,c,g = stdin.readline().split()
    s,c,g = int(s),int(c),int(g)
    if e == "MISS":
        c,g = -c,-g
    events.append((s,c,g))
k = int(stdin.readline())
lc,lg = 0,0
for s,c,g in events:
    if s <= k:
        lc += c
        lg += g
stdout.write(f"{lc} {lg}\n")
