from sys import stdin,stdout
    
# code runs in O(N + M) time
N,M = map(int,stdin.readline().split())
message = stdin.readline().split()
adjList,counter,mappings,revMappings = [],0,{},{}
for i in range(M):
    a,b = stdin.readline().split()
    if a not in mappings:
        mappings[a] = counter
        revMappings[counter] = a
        counter += 1
        adjList.append([])
    if b not in mappings:
        mappings[b] = counter
        revMappings[counter] = b
        counter += 1
        adjList.append([])
    u,v = mappings[a],mappings[b]
    adjList[u].append(v)
    adjList[v].append(u)

components,CC,lowest_per_cc = [-1 for i in range(counter)],0,{}
for i in range(counter):
    if components[i] == -1:
        frontier,L = [i],len(revMappings[i])
        while frontier:
            u = frontier.pop()
            for v in adjList[u]:
                if components[v] == -1:
                    components[v] = CC
                    frontier.append(v)
                    L = min(L, len(revMappings[v]))
        lowest_per_cc[CC] = L
        CC += 1

print(sum(lowest_per_cc[components[mappings[w]]] if w in mappings else len(w) for w in message))
