from sys import stdin,stdout
from collections import deque

def brexit(X,L,adjSet,leftUnion,originalPartners):   
    deleted = deque([L]) #treat as a queue
    leftUnion[L] = True
    while deleted: #O(P + C)
        u = deleted.popleft()
        if u == X:
            return "leave"
        for v in adjSet[u]:
            if not leftUnion[v]:
                adjSet[v].remove(u)
                if len(adjSet[v]) <= originalPartners[v]/2: #at least 50% of partners have left
                    leftUnion[v] = True
                    deleted.append(v)
    return "stay"
                
C,P,X,L = map(int,stdin.readline().split())
X -= 1; L -= 1; #offset by 1 due to zero indexing
adjSet,leftUnion = [set() for _ in range(C)],[False for _ in range(C)]
for _ in range(P):
    A,B = map(int,stdin.readline().split())
    adjSet[A-1].add(B-1)
    adjSet[B-1].add(A-1)
originalPartners = [len(adjSet[i]) for i in range(C)] #stores number of original partners of each country
stdout.write(brexit(X,L,adjSet,leftUnion,originalPartners))

