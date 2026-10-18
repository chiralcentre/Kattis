from sys import stdin,stdout


# model problem as graph problem, where vertices are the indices, and a directed edge exists from vertex a to vertex b if vertex b is the nearest block to the left/right of a strictly taller than a.
# resultant graph is a DAG, and there are most two edges per vertex
# reverse direction of the edges, we still have a DAG
# run shortest path algorithm for DAG in O(N) time after obtaining toposort in O(N) time
data = stdin.buffer.read().split()
N = int(data[0])
heights = list(map(int, data[1:N + 1]))
revAdjList,indeg = [[] for _ in range(N)],[0 for _ in range(N)]
left_stack,right_stack = [0],[N - 1]
for i in range(1,N):
    while left_stack and heights[left_stack[-1]] <= heights[i]:
        left_stack.pop()
    if left_stack:
        revAdjList[left_stack[-1]].append(i)
        indeg[i] += 1
    left_stack.append(i)
for i in range(N - 2, -1, -1):
    while right_stack and heights[right_stack[-1]] <= heights[i]:
        right_stack.pop()
    if right_stack:
        revAdjList[right_stack[-1]].append(i)
        indeg[i] += 1
    right_stack.append(i)
# perform shortest path on DAG in O(N) time
INF = pow(10,18)
D = [INF for _ in range(N)]
frontier = []
for v in range(len(indeg)):
    if indeg[v] == 0:
        frontier.append(v)
        D[v] = 0
while frontier:
    new_frontier = []
    for u in frontier:
        for v in revAdjList[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                new_frontier.append(v)
            D[v] = min(D[v],D[u] + 1)
    frontier = new_frontier
stdout.write(" ".join(str(num) for num in D))
