from sys import stdin

def kahnsAlgorithm(adjList,indeg):
    frontier = []
    for v in range(len(indeg)):
        if indeg[v] == 0:
            frontier.append(v)
    toposort = []
    while frontier:
        new_frontier = []
        for u in frontier:
            toposort.append(u)
            for v in adjList[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    new_frontier.append(v)
        frontier = new_frontier
    return toposort

# code runs in O(V + E) time, where E <= 1000 and V = number of unique UTF-8 characters
N = int(stdin.readline())
# UTF-8 is 4 byte encoding, so each string is maximum 500 characters
# mappings[char] = idx
# rev_mappings[idx] = char
mappings,rev_mappings,adjList,indeg = {},[],[],[]
prev = None
for i in range(N):
    S = stdin.readline().strip("\n")
    for char in S:
        if char not in mappings:
            mappings[char] = len(rev_mappings)
            rev_mappings.append(char)
            adjList.append(set())
            indeg.append(0)
    if prev != None:
        for i in range(min(len(S),len(prev))):
            if prev[i] != S[i]:
                a,b = mappings[prev[i]],mappings[S[i]]
                if b not in adjList[a]:
                    adjList[a].add(b)
                    indeg[b] += 1
                break
    prev = S

toposort = kahnsAlgorithm(adjList,indeg)
if len(toposort) != len(adjList):
    print("IMPOSSIBLE")
else:
    for i in range(1,len(toposort)):
        if toposort[i] not in adjList[toposort[i - 1]]:
            print("AMBIGUOUS")
            break
    else:
        print("".join(rev_mappings[idx] for idx in toposort))
