from sys import stdin,setrecursionlimit

setrecursionlimit(100000)
INF = float("inf")

# code runs in O(nT) time
def min_cost_cover(pairs, T):
    n = len(pairs)
    memo = [[None for _ in range(T + 1)] for j in range(n)]
    def recurse(i,r):
        if r <= 0:
            return 0
        if i == n:
            return INF
        if memo[i][r] != None:
            return memo[i][r]
        v,d = pairs[i]
        # at every index,we have two choices
        # choice one: do not take the state
        # choice two: take the state
        res = min(recurse(i + 1, r), v + recurse(i + 1, r - d))
        memo[i][r] = res
        return res
    result = recurse(0,T)
    return None if result == INF else result

def solve():
    S = int(stdin.readline())
    total,confirm,swing = 0,0,[]
    for _ in range(S):
        D,C,F,U = map(int,stdin.readline().split())
        total += D
        T = C + F + U
        W = T // 2 + 1
        if C >= W: # sure win
            confirm += D
        else: # C < W
            R = W - C
            if R <= U: # possible to win
                swing.append((R,D))
    needed = total // 2 + 1 - confirm
    if needed <= 0:
        return "0"
    else:
        cost = min_cost_cover(swing,needed)
        return "impossible" if cost is None else str(cost)

print(solve())
