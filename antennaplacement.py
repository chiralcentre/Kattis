from sys import stdin,stdout
import random

movements = [(-1,0),(0,1),(1,0),(0,-1)]
def possiblepositions(i,j,r,c):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]


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

# Split (i,j)th cell based on white black pattern
# if (i + j) % 2 = 0, the cell is white, else black
# We can model a graph with nodes representing the white and black cells, with edges between the cells if antenna can be placed between them
# The graph is now bipartite with two sets of nodes (white, black), since color of cells always changes between adjacent cells
# Problem is reduced to maximum independent set problem on the bipartite graph
# By Konig's theorem, |MVC| = |MCBM| for bipartite graph
# |MIS| = V - |MVC| = V - |MCBM|, where V = number of * characters
# Code runs in O(VE) = O(V * 4V) = O(V^2) = O(h^2 * w^2)
for k in range(int(stdin.readline())):
    h,w = map(int,stdin.readline().split())
    grid = [stdin.readline().strip() for _ in range(h)]
    white,black = [],[]
    white_mappings,black_mappings = {},{}
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "*":
                if not (i + j) % 2:
                    white.append((i,j))
                else:
                    black.append((i,j))
    for i in range(len(white)):
        x,y = white[i]
        white_mappings[x * 50 + y] = i
    for i in range(len(black)):
        x,y = black[i]
        black_mappings[x * 50 + y] = i + len(white)
    V = len(white) + len(black)
    match,AL = [-1 for _ in range(V)],[[] for _ in range(V)]
    for a,b in white:
        for x,y in possiblepositions(a,b,h,w):
            if x * 50 + y in black_mappings:
                AL[white_mappings[a * 50 + b]].append(black_mappings[x * 50 + y])
    MCBM = 0
    # greedy preprocessing to remove trivial augmenting paths
    freeV = {L for L in range(len(white))}
    match = [-1] * V
    for L in range(len(white)):
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
        vis = [0 for i in range(len(white))]
        MCBM += Aug(f)
    stdout.write(f"{V - MCBM}\n")
