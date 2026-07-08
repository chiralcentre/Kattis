from sys import stdin,stdout

freq = {}
for _ in range(int(stdin.readline())):
    route,h = stdin.readline().split()
    h = int(h)
    d = freq.get(route,{})
    d[h] = d.get(h,0) + 1
    freq[route] = d
routes = sorted(freq.keys())
for r in routes:
    d = freq[r]
    best,out = -1,None
    for k,v in d.items():
        if v > best:
            best,out = v,k
        elif v == best and k < out:
            out = k
    stdout.write(f"{r} {out}\n")
