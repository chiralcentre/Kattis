from sys import stdin,stdout

n,m = map(int,stdin.readline().split())
languages,counter = {"English": 0},1
for L in stdin.readline().split():
    languages[L] = counter
    counter += 1
adjList = [[] for _ in range(n+1)] # there are n+1 languages in total
for i in range(m):
    L1,L2,c = stdin.readline().split()
    a,b = languages[L1],languages[L2]
    adjList[a].append((b,int(c)))
    adjList[b].append((a,int(c))) 

visited,frontier = [False for _ in range(n+1)],[0] #start from the English language
visited[0] = True; totalVisited,totalCost = 1,0
while frontier: #BFS with time complexity O(n+m)
    newFrontier,lowestCost = [],{} #newFrontier contains all vertices one edge away from vertices in frontier
    for u in frontier: #left to right
        for v,c in adjList[u]:
            if not visited[v]:
                visited[v] = True
                totalVisited += 1
                newFrontier.append(v)
                lowestCost[v] = c
            elif v in lowestCost: 
                if c < lowestCost[v]: # cheaper alternative given same number of edges away from source
                    lowestCost[v] = c
    totalCost += sum(lowestCost.values())#O(m) at worst
    frontier = newFrontier
stdout.write(f'{totalCost}') if totalVisited == n+1 else stdout.write('Impossible')
