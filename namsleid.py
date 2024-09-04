from sys import stdin,stdout

# run Kahn's algorithm in O(n + m) time where n is number of courses and m is total number of edges
def kahnsAlgorithm(adjList,indeg):
    frontier,seen = [],0
    for v in range(len(indeg)):
        if indeg[v] == 0:
            frontier.append(v)
            seen += 1
    toposort = []
    while frontier:
        toposort.append(frontier)
        new_frontier = []
        for u in frontier:
            for v in adjList[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    new_frontier.append(v)
                    seen += 1
        frontier = new_frontier
    return seen,toposort  

n = int(stdin.readline())
adjList,indeg = [[] for _ in range(n)],[0 for _ in range(n)]
for i in range(n):
    m,*prereq = map(int,stdin.readline().split())
    for v in prereq:
        indeg[i] += 1
        adjList[v - 1].append(i)

seen,toposort = kahnsAlgorithm(adjList,indeg)
if seen != n:
    stdout.write("Omogulegt!\n")
else:
    stdout.write("Mogulegt!\n")
    stdout.write(f"{len(toposort)}\n")
    for lst in toposort:
        stdout.write(f"{len(lst)} ")
        stdout.write(" ".join(str(x + 1) for x in lst))
        stdout.write("\n")
