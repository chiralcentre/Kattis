from sys import stdin,stdout,setrecursionlimit
setrecursionlimit(10**8)

def backtrack(u,maximum):
    if u == len(colours):
        return True
    if colours[u] != 0: #coloured already
        return backtrack(u+1,maximum)
    for c in range(1,maximum+1):
        flag = False
        for v in adjList[u]:
            if colours[v] == c:
                flag = True
                break
        if flag:
            continue
        colours[u] = c
        if backtrack(u+1,maximum):
            return True
        colours[u] = 0 #reset to unexplored state
    return False
            

# Computing the chromatic number for general graphs is NP-complete (no efficient algorithm is known).
N = int(stdin.readline())
adjList,colours = [[] for _ in range(N)],[0 for _ in range(N)]
complete = True
for i in range(N):
    neighbours = list(map(int,stdin.readline().split()))
    adjList[i] = neighbours
    if len(neighbours) < N - 1:
        complete = False
#there is a minimum of 2 colours, and a maximum of N colours
#for a complete graph, N colours are required
if complete:
    stdout.write(f"{N}")
else:
    #j = maximum number of colours
    for j in range(2,N+1):
        #fix the colours of two arbitrary node as 1 and 2
        colours[0] = 1
        colours[adjList[0][0]] = 2
        #check if graph can be coloured with maximum number of colours
        if backtrack(1,j):
            stdout.write(f"{j}")
            break
