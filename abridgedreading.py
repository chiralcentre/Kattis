from sys import stdin,stdout

n,m = map(int,stdin.readline().split())
pages = []
while len(pages) < n:
    lst = list(map(int,stdin.readline().split()))
    pages.extend(lst)
adjList,CC = [-1 for _ in range(n)],{i for i in range(n)}
for i in range(m):
    u,v = map(lambda x: int(x) - 1, stdin.readline().split())
    #every vertex has at most one parent
    adjList[v] = u #the edges directions are reversed
    CC.discard(u)
#CC contains list of possible culminating concept chapters
CC,lowest = list(CC),10**9
#O(n^2) worst case occurs when all chapters are culminating concept chapters
for i in range(len(CC)):
    u = CC[i]
    t,read = 0,set()
    while u != -1:
        read.add(u)
        t += pages[u]
        u = adjList[u]
    for j in range(i + 1,len(CC)):
        v,temp = CC[j],t
        while v != -1 and v not in read:
            temp += pages[v]
            v = adjList[v]   
        lowest = min(lowest,temp)
stdout.write(f"{lowest}\n")
