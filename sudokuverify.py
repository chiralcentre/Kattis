def verify(grid):
    # row check
    for i in range(9):
        nums = {grid[i][j] for j in range(9)}
        if len(nums) != 9:
            return "INVALID!"
    # columns check
    for j in range(9):
        nums = {grid[i][j] for i in range(9)}
        if len(nums) != 9:
            return "INVALID!"
    # 3 x 3 region check
    for i in range(0,9,3):
        for j in range(0,9,3):
            nums = {grid[m][n] for m in range(i, i + 3) for n in range(j, j + 3)}
            if len(nums) != 9:
                return "INVALID!"
    return "VALID"

print(verify([list(map(int,input().split())) for _ in range(9)]))
