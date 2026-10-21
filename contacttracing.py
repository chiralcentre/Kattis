from sys import stdin,stdout

# model problem as graph problem
# vertices are indices of people, an undirected edge exists between two people if their intervals overlap
N,D = map(int,stdin.readline().split())
_,*infected = map(lambda x: int(x) - 1,stdin.readline().split())
events = []
for i in range(N):
    s,t = map(int,stdin.readline().split())
    events.append((s,0,i))
    events.append((t,1,i))
# sort by start time in O(N log N) time
events.sort()
adjList = [[] for _ in range(N)]
active = set()
for _,kind,i in events:
    if kind == 0:
        for j in active: # size of active set is at most 50, O(1) time
            adjList[i].append(j)
            adjList[j].append(i)
        active.add(i)
    else:
        active.discard(i)

# BFS from infected people in O(V + E) = O(N) time
frontier,visited,days = [],[False for _ in range(N)],0
for x in infected:
    frontier.append(x)
    visited[x] = True
while frontier and days < D:
    new_frontier = []
    for u in frontier:
        for v in adjList[u]:
            if not visited[v]:
                visited[v] = True
                infected.append(v)
                new_frontier.append(v)
    frontier = new_frontier
    days += 1
stdout.write(" ".join(str(num + 1) for num in sorted(infected)))
