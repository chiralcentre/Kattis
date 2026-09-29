from sys import stdin

# Sort all components by g in descending order and add them one at a time
# Right after adding a component with performance g, check whether all k types are covered and the sum is <= p.
# The first time this holds, g is the answer. It is achievable, because every chosen component has performance >= g.
n,k,p = map(int,stdin.readline().split())
names = stdin.readline().strip().split()
components = []
for _ in range(n):
    s,v,g = stdin.readline().split()
    components.append((s,int(v),int(g)))
components.sort(key = lambda x: -x[2])
# P[s] = t -> current cheapest price for component of type s is t
# C = running sum of per type minimums
P,C = {},0
for s,v,g in components:
    if s not in P:
        C += v
        P[s] = v
    elif P[s] > v:
        C += v - P[s]
        P[s] = v
    if len(P) == len(names) and C <= p:
        print(g)
        break
else:
    print("O nei!")
