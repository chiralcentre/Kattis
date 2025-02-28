from sys import stdin

def valid_solution(markings,d):
    if markings.get(0,-1) != 1 or len(markings) != d + 1:
        return 0
    markings.pop(0)
    for key,value in markings.items():
        if value != 3:
            return 0
    return 1

def solve():
    n = int(stdin.readline())
    d = (pow(4,n) - 1) // 3
    L = pow(2,n)
    grid = [list(map(int,stdin.readline().split())) for _ in range(L)]
    visited,markings = [[False for i in range(L)] for j in range(L)],{}
    for i in range(L):
        for j in range(L):
            if not visited[i][j] and grid[i][j] != 0:
                visited[i][j] = True
                found = False
                # check first,second,third shapes
                if i + 1 < L and j + 1 < L:
                    if grid[i][j] == grid[i][j + 1] == grid[i + 1][j]:
                        visited[i][j + 1] = True
                        visited[i + 1][j] = True
                        found = True
                    elif grid[i][j] == grid[i][j + 1] == grid[i + 1][j + 1]:
                        visited[i][j + 1] = True
                        visited[i + 1][j + 1] = True
                        found = True
                    elif grid[i][j] == grid[i + 1][j] == grid[i + 1][j + 1]:
                        visited[i + 1][j] = True
                        visited[i + 1][j + 1] = True
                        found = True
                # check fourth shape
                if i + 1 < L and j - 1 >= 0 and grid[i][j] == grid[i + 1][j] == grid[i + 1][j - 1]:
                    visited[i + 1][j] = True
                    visited[i + 1][j - 1] = True
                    found = True
                if not found:
                    return 0
            markings[grid[i][j]] = markings.get(grid[i][j],0) + 1
    return valid_solution(markings,d)


print(solve())
