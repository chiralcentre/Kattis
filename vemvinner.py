from sys import stdin

winners = {"X": "Johan har vunnit", "O": "Abdullah har vunnit"}

def solve(grid):
    # check rows
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] in winners:
            return winners[grid[i][0]]
    # check columns
    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] in winners:
            return winners[grid[0][i]]
    # check diagonals
    if (grid[0][0] == grid[1][1] == grid[2][2] or grid[2][0] == grid[1][1] == grid[0][2]) and grid[1][1] in winners:
        return winners[grid[1][1]]
    return "ingen har vunnit"

grid = [stdin.readline().strip().split() for i in range(3)]
print(solve(grid))
