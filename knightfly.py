from sys import stdin

movements = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
def possiblepositions(u,up,down,left,right):
    res = []
    def traverse(x,y,u,A,B):
        s = u
        order = ((A,2),(B,1)) if abs(x) == 2 else ((B,2),(A,1))
        for arr, k in order:
            for _ in range(k):
                s = arr[s]
                if s == -1:
                    return -1
        return s
    for x,y in movements:
        A = right if x > 0 else left
        B = up if y > 0 else down
        s = traverse(x,y,u,A,B)
        if s != -1:
            res.append(s)
    return res
        
# code runs in O(N log N) time, N vertices, maximum 8N edges
def solve():
    N = int(stdin.readline())
    xs,ys,xt,yt = map(int,stdin.readline().split())
    mappings,x_group,y_group = {},{},{}
    for i in range(N):
        a,b = map(int,stdin.readline().split())
        mappings[(a,b)] = i
        if a not in x_group:
            x_group[a] = [b]
        else:
            x_group[a].append(b)
        if b not in y_group:
            y_group[b] = [a]
        else:
            y_group[b].append(a)
    if (xs,ys) not in mappings or (xt,yt) not in mappings:
        return -1
    if (xs,ys) == (xt,yt):
        return 0
    up,down,left,right = [-1 for _ in range(N)],[-1 for _ in range(N)],[-1 for _ in range(N)],[-1 for _ in range(N)]
    for x in x_group:
        L = sorted(x_group[x])
        pos = [mappings[(x,y)] for y in L]
        for i in range(len(L) - 1):
            up[pos[i]] = pos[i + 1]
        for i in range(len(L) - 1,0,-1):
            down[pos[i]] = pos[i - 1]
    for y in y_group:
        L = sorted(y_group[y])
        pos = [mappings[(x,y)] for x in L]
        for i in range(len(L) - 1):
            right[pos[i]] = pos[i + 1]
        for i in range(len(L) - 1,0,-1):
            left[pos[i]] = pos[i - 1]
    start,end = mappings[(xs,ys)],mappings[(xt,yt)]
    frontier,moves = [start],0
    visited = [False for _ in range(N)]
    visited[start] = True
    while frontier:
        new_frontier = []
        for u in frontier:
            for v in possiblepositions(u,up,down,left,right):
                if not visited[v]:
                    if v == end:
                        return moves + 1
                    visited[v] = True
                    new_frontier.append(v)
        moves += 1
        frontier = new_frontier
    return -1

print(solve())
