from sys import stdin
from collections import deque

#preconditions:
#1) graph must be directed acyclic
#2) adjList is a list of lists representing the graph in adjaceny list form
#3) indeg is a list of length V where indeg[v] represents the indegree of vertex v
#postconditions:
#1) indeg array is modified such that every entry is now 0
#2) returns an list of vertices in topological order
def kahnsAlgorithm(adjList,indeg):
    frontier = deque([])
    for v in range(len(indeg)):
        if indeg[v] == 0:
            frontier.append(v)
    toposort = []
    while frontier:
        u = frontier.popleft()
        toposort.append(u)
        for v in adjList[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                frontier.append(v)
    return toposort

def find_edge(w1,w2):
    for i in range(min(len(w1),len(w2))):
        if w1[i] != w2[i]:
            return w1[i],w2[i]
    return None,None

# let there be 26 nodes representing every letter in the alphabet
# a directed edge exists between node u towards v if u is lexicographically smaller than v
# if a cycle exists, its impossible to determine, else output toposort
# code runs in O(n + L) time when L is total length of strings
# time taken for toposort is taken to be constant since V is fixed at 26
n = int(stdin.readline())
adjList = [[] for i in range(26)]
indeg = [0 for i in range(26)]
lines = [stdin.readline().strip() for i in range(n)]
for i in range(n - 1):
    w1,w2 = lines[i],lines[i + 1]
    u,v = find_edge(w1,w2)
    if (u,v) != (None, None): # edge found
        c1,c2 = ord(u) - 97, ord(v) - 97
        adjList[c1].append(c2)
        indeg[c2] += 1
    elif len(w1) > len(w2):
        # no edge found and w1 is longer than w2
        # not possible
        print("impossible")
        exit(0)
toposort = kahnsAlgorithm(adjList,indeg)
if len(toposort) == 26: # direct acyclic graph
    print("".join(chr(code + 97) for code in toposort))
else: # cycle found
    print("impossible")
        
