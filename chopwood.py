from sys import stdin,stdout
from heapq import heapify,heappush,heappop

def solve():
    n = int(stdin.readline())
    deg = [1 for i in range(n + 1)] #there are n + 1 vertices in the tree, if it exists
    order = []
    for i in range(n):
        # ignore last line 
        v = int(stdin.readline()) - 1
        order.append(v)
        if i < n - 1:
            deg[v] += 1
    PQ = [i for i in range(n + 1) if deg[i] == 1]
    heapify(PQ)
    seen,ans = set(),[]
    for i in range(n):
        if order[i] not in seen:
            a = heappop(PQ)
            ans.append(a + 1)
            seen.add(a)
            deg[order[i]] -= 1
            if deg[order[i]] == 1:
                heappush(PQ,order[i])
        else:
            stdout.write("Error\n")
            return
    stdout.write("\n".join(str(u) for u in ans))
    
solve()
