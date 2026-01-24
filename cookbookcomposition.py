from sys import stdin,stdout
from collections import deque
from fractions import Fraction

# code runs in O(n(s + ds))
def critical_path(adjList,indeg,values):
    dp = values[:] # dp[v] = longest path ending at v
    q = deque([])
    for i in range(len(indeg)):
        if indeg[i] == 0:
            q.append(i)
    while q:
        u = q.popleft()
        for v in adjList[u]:
            dp[v] = max(dp[v], dp[u] + values[v])
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return max(dp)

n = int(stdin.readline())
recipes = []
for i in range(n):
    recipe,s = stdin.readline().split()
    indeg,seen,values,adjList,total = [],{},[],[],0
    for j in range(int(s)):
        step,t,_,*deps = stdin.readline().split()
        if step not in seen:
            seen[step] = len(indeg)
            values.append(int(t))
            total += values[-1]
            indeg.append(0)
            adjList.append([])
        v = seen[step]
        for d in deps:
            u = seen[d]
            indeg[v] += 1
            adjList[u].append(v)
    recipes.append((Fraction(total,critical_path(adjList,indeg,values)), recipe))
    
recipes.sort(key = lambda x: x[0])
for _,name in recipes:
    stdout.write(f"{name}\n")
