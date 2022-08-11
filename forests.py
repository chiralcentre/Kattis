from sys import stdin,stdout

P,T = map(int,stdin.readline().split())
adjList = [[] for _ in range(P)]
for line in stdin:
    i,j = map(int,line.split())
    i -= 1
    adjList[i].append(j)
opinions = {tuple(sorted(lst)) for lst in adjList}
stdout.write(str(len(opinions)))
