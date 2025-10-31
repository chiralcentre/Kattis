from sys import stdin

def solve():
    n,m,k = map(int,stdin.readline().split())
    adjList = [[] for _ in range(n)]
    for i in range(m):
        a,b = map(lambda x: int(x) - 1, stdin.readline().split())
        adjList[a].append(b)
        adjList[b].append(a)
    # find every connected component, check if its possible to assign each game variant to every kid in the component
    labels = [-1 for _ in range(n)]
    for i in range(n):
        if labels[i] == -1:
            counter = 1
            frontier = [i]
            labels[i] = counter
            while frontier:
                u = frontier.pop()
                for v in adjList[u]:
                    if labels[v] == -1:
                        counter += 1
                        labels[v] = counter % k if counter % k > 0 else k
                        frontier.append(v)
            if counter < k:
                return "impossible"
    return " ".join(str(num) for num in labels)

print(solve())
