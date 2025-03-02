from sys import stdin,stdout

def DFS_rec(adjList,u):
    global founder_blood
    if founder_blood[u] != -1:
        return founder_blood[u]
    if len(adjList[u]) == 0:
        if founder_blood[u] == -1:
            founder_blood[u] = 0
        return founder_blood[u]
    total = 0
    for v in adjList[u]:
        total += (DFS_rec(adjList,v) >> 1)
    return total
        
def update_counter(p,mappings,counter):
    if p not in mappings:
        mappings[p] = counter
        counter += 1
    return counter
    
N,M = map(int,stdin.readline().split())
founder = stdin.readline().strip()
mappings,counter = {},0
mappings[founder] = counter
counter += 1
relations = []
for i in range(N):
    c,p1,p2 = stdin.readline().split()
    counter = update_counter(c,mappings,counter)
    counter = update_counter(p1,mappings,counter)
    counter = update_counter(p2,mappings,counter)
    relations.append((mappings[c],mappings[p1],mappings[p2]))
adjList = [[] for _ in range(counter)]
for c,a,b in relations:
    adjList[c].append(a)
    adjList[c].append(b)

founder_blood = [-1 for i in range(counter)]
founder_blood[0] = pow(2, 70) # use arbitrary large number, note founder_blood percentage cannot exceed 2^50
highest,best = -1,""
for i in range(M):
    w = stdin.readline().strip()
    if w in mappings:
        blood_value = DFS_rec(adjList,mappings[w])
        if blood_value > highest:
            highest,best = blood_value,w
print(best)
    
    
    

