from sys import stdin,stdout

for t in range(int(stdin.readline())):
    if t > 0: stdout.write("\n") #print blank line between test cases
    stdin.readline() #read in blank line
    N,M = map(int,stdin.readline().split())
    adjSet,deg = [set() for i in range(N)],[0 for i in range(N)]
    for i in range(M): #O(M)
        u,v,w = map(int,stdin.readline().split())
        u -= 1; v -= 1 #offset by 1 due to zero indexing
        deg[u] += 1; deg[v] += 1
        adjSet[u].add((v,w)); adjSet[v].add((u,w))
    #bypass vertices with degree of 2 in O(N) time
    for i in range(N):
        if deg[i] == 2: #only connected to two other vertices
            u1,w1 = adjSet[i].pop(); u2,w2 = adjSet[i].pop()
            adjSet[u1].remove((i,w1)); adjSet[u1].add((u2,w1+w2))
            adjSet[u2].remove((i,w2)); adjSet[u2].add((u1,w1+w2))
    pairs = set() #keep track of which pair of stations has appeared before
    roads = []
    for u in range(N): #O(N + M)
        for v,w in adjSet[u]: 
            if (v,u) not in pairs: #no need to check if (u,v) is present since there are no duplicate pairs in same orientation
                pairs.add((u,v))
                roads.append(f"{u+1} {v+1} {w}\n") #add back 1
    stdout.write(f"{len(roads)}\n")
    for r in roads: stdout.write(r)
               
            
