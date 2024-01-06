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

# Each book is read by exactly one boy and one girl
# We can model a graph with nodes representing boys and girls, and an edge exists between boy a and girl b if a and b are reading the same book
# The graph is now bipartite with two sets of nodes (boys, girls)
# Problem is reduced to minimum vertex cover problem on the bipartite graph
# By Konig's theorem, |MVC| = |MCBM| for bipartite graph
# Code runs in O(VE) 
B,G = map(int,stdin.readline().split())
match,AL = [-1 for _ in range(B + G)],[[] for _ in range(B + G)]
read_by = {}
for i in range(B):
    name,num,*books = stdin.readline().split()
    for b in books:
        read_by[b] = i # book b is read by boy i
for i in range(G):
    name,num,*books = stdin.readline().split()
    for b in books:
        AL[read_by[b]].append(B + i) # single edge from boy to girl reading the same book

MCBM = 0
# greedy preprocessing to remove trivial augmenting paths
freeV = {L for L in range(B)}
match = [-1] * (B + G)
for L in range(B):
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
    vis = [0 for i in range(B)]
    MCBM += Aug(f)
stdout.write(f"{MCBM}\n")
