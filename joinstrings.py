from sys import stdin,stdout,setrecursionlimit
from collections import deque
# increase recursion limit
setrecursionlimit(10**6)

def recursive_graph_transversal(graphs,strings,last_index):
    #directed graph traversal
    stdout.write(strings[last_index])
    while graphs[last_index]: #while not empty
        vertex = graphs[last_index].popleft()
        recursive_graph_transversal(graphs,strings,vertex)
    
strings,last_index = [],-1
for linenum,line in enumerate(stdin):
    if linenum == 0:
        N = int(line)
        if N == 1:
            continue
        graph = [deque([]) for _ in range(N)]
    elif 0 < linenum <= N:
        strings.append(line.strip())
        if N == 1:
            print(strings[0])
            break
    elif N < linenum <= 2*N - 1:
        a,b = map(int,line.split())
        a -= 1; b -= 1 #offset by 1
        graph[a].append(b) # a points to b
        last_index = a
        if linenum == 2*N - 1:
            break
    
if N > 1:        
    recursive_graph_transversal(graph,strings,last_index)



