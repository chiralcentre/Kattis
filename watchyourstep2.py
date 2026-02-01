def n_ways_with_blocks(sx, sy, ex, ey, blocks):
    # use top down dynamic programming
    memo = [[-1 for i in range(ey + 1)] for j in range(ex + 1)]
    obstacles = set(blocks)
    def recurse(a,b):
        if memo[a][b] != -1:
            return memo[a][b]
        if (a,b) in obstacles:
            memo[a][b] = 0
        elif (a,b) == (sx,sy):
            memo[a][b] = 1
        else:
            memo[a][b] = 0
            if a > 0:
                memo[a][b] += recurse(a - 1, b)
            if b > 0:
                memo[a][b] += recurse(a, b - 1)
        return memo[a][b]
    return recurse(ex, ey)

sx,sy,ex,ey,mx,my,nx,ny = map(int,input().split())
blocks = {(mx,my),(nx,ny)}
print(n_ways_with_blocks(sx, sy, ex, ey, blocks))
