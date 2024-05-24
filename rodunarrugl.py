from sys import stdin

n = int(stdin.readline())
placings = list(map(lambda x: int(x) - 1, stdin.readline().split()))
visited = [False for i in range(n)]
ans = 0
for i in range(n):
    if not visited[i] and placings[i] != i:
        s = placings[i]
        # form cycles
        while s != i:
            ans += 1
            visited[s] = True
            s = placings[s]
        # with cycle length of n, n + 1 moves are needed to move everything into the right place
        ans += 2 
        visited[i] = True
print(ans)
