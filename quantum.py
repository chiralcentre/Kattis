from sys import stdin,stdout
from heapq import heappush,heappop

INF = 1000000000 #use 1 billion to represent infinity

def quantum(op,w):
    for i in range(len(op)):
        j = len(op) - i - 1
        if op[i] == "F":
            w ^= (1 << j)
        elif op[i] == "S":
            w |= (1 << j)
        elif op[i] == "C":
            w &= ~(1 << j)
    return w

def modifiedDjikstra(ops,N,s,e):
    D = [INF for _ in range(N)]; D[s] = 0
    PQ = []; heappush(PQ,(0,s))
    while PQ:
        d,u = heappop(PQ)
        if u == e:
            return str(d)
        if d == D[u]: # check if this is the superior copy
            for s,w in ops:
                v = quantum(s,u)
                if D[v] > D[u] + w: # can relax
                    D[v] = D[u] + w
                    heappush(PQ,(D[v],v))
    return "NP"

for _ in range(int(stdin.readline())):
    L,nop,nw = map(int,stdin.readline().split())
    ops,ans = [],[]
    for i in range(nop):
        q,c = stdin.readline().split()
        c = int(c)
        ops.append((q,c))
    N = pow(2,L) # use a bitmask of length L
    for i in range(nw):
        s,e = stdin.readline().split()
        s,e = int(s,2),int(e,2) # convert from binary to decimal
        ans.append(modifiedDjikstra(ops,N,s,e))
    stdout.write(" ".join(a for a in ans))
    stdout.write("\n")
