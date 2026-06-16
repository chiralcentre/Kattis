from sys import stdin

def solve():
    n = int(stdin.readline())
    grid = []
    for r in range(4):
        grid.append(list(map(int, stdin.readline().split())))
    valid = [m for m in range(16) if not (m & (m >> 1))]  # 8 masks
    NEG_INF = float('-inf')
    # m >> r & 1 extracts bit r from mask m
    dp = {m: sum(grid[r][0] for r in range(4) if m >> r & 1) for m in valid}
    for j in range(1, n):
        col = {m: sum(grid[r][j] for r in range(4) if m >> r & 1) for m in valid}
        new_dp = {m: NEG_INF for m in valid}
        for m in valid:
            for pm in valid:
                if not (m & pm):  # compatible with previous column
                    val = dp[pm] + col[m]
                    if val > new_dp[m]:
                        new_dp[m] = val
        dp = new_dp
    return max(dp.values())

print(solve())
