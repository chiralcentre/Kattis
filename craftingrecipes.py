from sys import stdin

# code runs in O(N + M) time
def recurse(mat,deps,cost):
    if mat in cost:
        return cost[mat]
    total = 0
    for m,w in deps[mat]:
        total += recurse(m,deps,cost) * w
    cost[mat] = total
    return total
    
N = int(stdin.readline())
cost = {}
for _ in range(N):
    mat,c = stdin.readline().split()
    cost[mat] = int(c)
M = int(stdin.readline())
deps = {}
# only one recipe per component
for _ in range(M):
    comp,P,*parts = stdin.readline().split()
    edges = []
    for i in range(int(P)):
        edges.append((parts[2 * i],int(parts[2 * i + 1])))
    deps[comp] = edges
print(recurse("Capstone",deps,cost))
