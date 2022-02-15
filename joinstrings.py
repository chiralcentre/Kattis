from sys import stdin,stdout,setrecursionlimit
from collections import deque
# increase recursion limit since default recursion limit is 1000 and N can be at most 10000
setrecursionlimit(10**7)

def recursive_graph_transversal(graphs,strings,last_index):
    #directed graph traversal
    stdout.write(strings[last_index])
    while graphs[last_index]: #while not empty
        recursive_graph_transversal(graphs,strings,graphs[last_index].popleft()) #graphs[last_index].popleft() =  next vertex
    
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
        graph[a-1].append(b-1) # #offset by 1; a-1 points to b-1
        last_index = a - 1
        
if N > 1:        
    recursive_graph_transversal(graph,strings,last_index)



