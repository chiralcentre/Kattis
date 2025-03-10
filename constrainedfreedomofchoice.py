from sys import stdin,stdout

def n_ways_with_blocks(A, B, grid):
    memo = [[0 for _ in range(B)] for i in range(A)]
    for i in range(A):
        if grid[i][0] == "#":
            break
        memo[i][0] = 1
    for c in range(1,B):
        vertical_start,curr_sum = 0,0
        for r in range(A):
            if grid[r][c] != "#":
                curr_sum += memo[r][c - 1]
                continue
            for r2 in range(vertical_start, r):
                memo[r2][c] = curr_sum
            vertical_start,curr_sum = r + 1,0
        for r2 in range(vertical_start, A):
            memo[r2][c] = curr_sum
    return memo[-1][-1]

while True:
    r,c = map(int,stdin.readline().split())
    if r == c == 0:
        break
    grid = [stdin.readline().strip() for _ in range(r)][::-1] # reverse the grid
    stdout.write(f"{n_ways_with_blocks(r,c,grid)}\n")
