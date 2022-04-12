from sys import stdin,stdout


def DFS(u,p,status,adjList): #u is current vertex, p is predecessor of u in DFS tree
    status[u] = "VISITING"
    for v in adjList[u]:
        if status[v] == "VISITING": #v != p condition is dropped since cycle in this case can be between two vertices
            global hasCycle #global keyword is used so that hasCycle is accessed within the DFS procedure
            hasCycle = True
            return
        DFS(v,u,status,adjList)
    status[u] = "VISITED"
    
n = int(stdin.readline())
cities,counter,adjList = {},0,[[] for _ in range(n)]
for _ in range(n):
    o,d = stdin.readline().split()
    if o not in cities:
        cities[o] = counter
        counter += 1
    if d not in cities:
        cities[d] = counter
        counter += 1
    adjList[cities[o]].append(cities[d])
    
while True:
    try:
        status,hasCycle = ["NOT VISITED" for _ in range(n)], False
        c = stdin.readline().strip()
        DFS(cities[c],cities[c],status,adjList)
        stdout.write(f'{c} safe\n') if hasCycle else stdout.write(f'{c} trapped\n')
    except:
        break
