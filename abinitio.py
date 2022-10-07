from sys import stdin,stdout
#time limit exceeded
V,E,Q = map(int,stdin.readline().split())
# inEdges[i] stores all vertices with edges pointing towards i, and outEdges[i] stores all vertices which i points towards
# inEdgesC and outEdgesC store information of graph complement
inEdges,outEdges = [set() for _ in range(V)],[set() for _ in range(V)]
inEdgesC,outEdgesC = [set(num for num in range(V) if num != i) for i in range(V)],[set(num for num in range(V) if num != i) for i in range(V)] #O(V^2)
for i in range(E):
    u,v = map(int,stdin.readline().split())
    inEdges[v].add(u); outEdges[u].add(v)
    inEdgesC[v].remove(u); outEdgesC[u].remove(v)

for i in range(Q):
    command,*rest = map(int,stdin.readline().split())
    if command == 1: #O(V)
        inEdges.append(set()); outEdges.append(set())
        for i in range(V):
            inEdgesC[i].add(V)
            outEdgesC[i].add(V)
        inEdgesC.append(set(num for num in range(V)))
        outEdgesC.append(set(num for num in range(V)))
        V += 1
    elif command == 2: #O(1)
        a,b = rest
        inEdges[b].add(a); outEdges[a].add(b)
        inEdgesC[b].remove(a); outEdgesC[a].remove(b)
    elif command == 3: #O(V)
        a = rest[0]
        for u in inEdges[a]:
            outEdges[u].remove(a)
            outEdgesC[u].add(a)
        for v in outEdges[a]:
            inEdges[v].remove(a)
            inEdgesC[v].add(a)
        inEdges[a].clear(); outEdges[a].clear()
        inEdgesC[a] = set(num for num in range(V)); inEdgesC[a].remove(a)
        outEdgesC[a] = set(num for num in range(V)); outEdgesC[a].remove(a)
    elif command == 4: #O(1)
        a,b = rest
        inEdges[b].remove(a); outEdges[a].remove(b)
        inEdgesC[b].add(a); outEdgesC[a].add(b)
    elif command == 5: #O(1)
        inEdges,outEdges = outEdges,inEdges
        inEdgesC,outEdgesC = outEdgesC,inEdgesC
    elif command == 6: #O(1)
        inEdges,inEdgesC = inEdgesC,inEdges
        outEdges,outEdgesC = outEdgesC,outEdges
    
stdout.write(f'{V}\n')
for i in range(V):
    out = sorted(outEdges[i]) #sorted returns a list
    h = sum(7**j*out[j] for j in range(len(out)))%(10**9+7)
    stdout.write(f'{len(out)} {h}\n')
