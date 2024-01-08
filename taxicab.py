from sys import stdin,stdout
import random

def Aug(L):
    global match, vis, AL
    if vis[L]:
        return 0
    vis[L] = 1
    for R in AL[L]:
        if match[R] == -1 or Aug(match[R]):
            match[R] = L
            return 1
    return 0

# create two nodes for each taxi, creating a bipartite graph with two sets U and V
# if same plane can be used for trips (a,b), put an edge between U_a and V_b
# every edge has capacity 1
# result of MCBM represents number of taxis that can be reused
# required answer = m - |MCBM|
for _ in range(int(stdin.readline())):
    m = int(stdin.readline())
    flights = []
    for i in range(m):
        time,a,b,c,d = stdin.readline().split()
        a,b,c,d = int(a),int(b),int(c),int(d)
        hours,mins = map(int,time.split(":"))
        flights.append((hours * 60 + mins,a,b,c,d))
    match,AL = [-1 for _ in range(m << 1)],[[] for _ in range(m << 1)]
    for i in range(m):
        for j in range(m):
            if i != j:
                ti,ai,bi,ci,di = flights[i]
                tj,aj,bj,cj,dj = flights[j]
                if ti + abs(ai - ci) + abs(bi - di) + abs(ci - aj) + abs(di - bj) < tj:
                    AL[i].append(j + m)
    MCBM = 0
    # greedy preprocessing to remove trivial augmenting paths
    freeV = {L for L in range(m)}
    for L in range(m):
        candidates = []
        for R in AL[L]:
            if match[R] == -1:
                candidates.append(R)
        if len(candidates) > 0:
            MCBM += 1
            freeV.remove(L)
            a = random.randrange(len(candidates))
            match[candidates[a]] = L
    for f in freeV: #for every unmatched white cell
        vis = [0 for i in range(m)]
        MCBM += Aug(f)
    stdout.write(f"{m - MCBM}\n")
