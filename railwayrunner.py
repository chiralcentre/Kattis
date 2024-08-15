from sys import stdin

adj_movements = [(0,1),(0,-1)]
def possible_positions(i,j,r,c,grid):
    pos = []
    # check if its possible to move to the left and right
    for x,y in adj_movements:
        if i + x in range(r) and j + y in range(c) and grid[i][j] != "/" and grid[i][j] == grid[i][j + y]:
            pos.append((i, j + y))
    # check if its possible to move to downwards
    if i + 1 in range(r) and not (grid[i][j] == "." and grid[i + 1][j] == "*"):
        pos.append((i + 1, j))
    return pos

# there are 3N vertices and maximum of 9N edges
# DFS runs in O(V + E) = O(N) time
def solve():
    N = int(stdin.readline())
    grid = [stdin.readline().strip() for _ in range(N)]
    visited = [[False for i in range(3)] for j in range(N)]
    frontier = []
    for i in range(3):
        if grid[0][i] == ".":
            visited[0][i] = True
            frontier.append((0,i))
    while frontier:
        i,j = frontier.pop()
        for x,y in possible_positions(i,j,N,3,grid):
            if not visited[x][y]:
                if x == N - 1:
                    return "YES"
                visited[x][y] = True
                frontier.append((x,y))
    return "NO"

if __name__ == "__main__":
    print(solve())
