def solve(N,M):
    # use BFS
    # V = 40000, E < 120000
    INF = pow(10,18)
    D = [INF for _ in range(40001)]
    frontier = [N]
    D[N] = 0
    while frontier:
        new_frontier = []
        for u in frontier:
            curr = D[u] + 1
            for v in [2 * u, u + 1, u - 1]:
                if v < len(D) and curr < D[v]:
                    D[v] = curr
                    new_frontier.append(v)
                    if v == M:
                        return curr
        frontier = new_frontier
    raise Exception("not supposed to happen")

N,M = map(int,input().split())
if M <= N:
    print(N - M) # subtract 1 until N is transformed into M
else:
    print(solve(N,M))
