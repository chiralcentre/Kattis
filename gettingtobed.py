from sys import stdin

movements = [(-1,0),(0,1),(1,0),(0,-1)]

def possiblepositions(i,j,r,c):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

def solve():
    n,m,k = map(int,stdin.readline().split())
    visited = [[False for _ in range(m)] for i in range(n)]
    for _ in range(k):
        x,y = map(int,stdin.readline().split())
        visited[x][y] = True
    fx,fy = map(int,stdin.readline().split())
    frontier = [(0,0)]
    visited[0][0] = True
    while frontier:
        a,b = frontier.pop()
        if a == fx and b == fy:
            return "SLEEPING"
        for x,y in possiblepositions(a,b,n,m):
            if not visited[x][y]:
                visited[x][y] = True
                frontier.append((x,y))
    return "IMPOSSIBLE"  

print(solve())
