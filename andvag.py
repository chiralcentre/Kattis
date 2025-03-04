from sys import stdin,stdout

# overall code runs in O(N + M + Q)
N,M,Q = map(int,stdin.readline().split())
adjList = [[] for _ in range(N)]
for i in range(M):
    u,v,w = map(int,stdin.readline().split())
    u -= 1; v -= 1 #offset by 1 due to zero indexing
    adjList[u].append((v,w))
    adjList[v].append((u,w))

components,largest_per_component,CC = [-1 for i in range(N)],{},0
# largest number of feathers cleaned between each pair is effectively the largest number of feathers cleaned in each component
for i in range(N):
    if components[i] == -1:
        frontier = [i]; s = 0
        components[i] = CC
        while frontier:
            u = frontier.pop()
            for v,w in adjList[u]:
                if components[v] == -1:
                    frontier.append(v)
                    components[v] = CC
                s |= w
        largest_per_component[CC] = s.bit_count()
        CC += 1
                    
for i in range(Q): #each query can be answered in O(1) time
    u,v = map(lambda x: int(x) - 1, stdin.readline().split()) #offset by 1 due to zero indexing
    stdout.write(f"{largest_per_component[components[u]]}\n") if components[u] == components[v] else stdout.write("-1\n")
