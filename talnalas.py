from sys import stdin,stdout

def increment(digit):
    return str((int(digit) + 1) % 10)

def decrement(digit):
    return str((int(digit) - 1) % 10)

def BFS(n,m,adjList,numbers):
    # time complexity of BFS = O(V + E) = O(m + 2nm)
    # start from vertex m as source
    frontier,visited,parent = [m],[False for _ in range(m + 2)],[-1 for _ in range(m + 2)]
    visited[m] = True
    while frontier:
        new_frontier = []
        for u in frontier:
            for v in adjList[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    new_frontier.append(v)
                    if v == m + 1: # end state reached
                        path,curr = [m + 1],m + 1
                        while parent[curr] != -1:
                            curr = parent[curr]
                            path.append(curr)
                        return [numbers[path[i]] for i in range(len(path) - 1, -1, -1)]        
        frontier = new_frontier
    return ["Neibb"]

n,m = map(int,stdin.readline().split())
start = stdin.readline().strip() 
end = stdin.readline().strip() 
adjList = [[] for _ in range(m + 2)]
numbers,mappings = [],{}
for i in range(m):
    num = stdin.readline().strip()
    numbers.append(num)
    mappings[num] = i
# assign starting vertex number of m
numbers.append(start)
mappings[start] = m
# assign ending vertex number of m + 1
numbers.append(end)
mappings[end] = m + 1
# generate all possible edges
# note that a maximum of 2*n edges can be generated per number
# O(nm) to generate all possible edges
for i in range(m + 2):
    num = list(numbers[i])
    for j in range(n):
        original = num[j]
        num[j] = increment(original)
        increment_num = "".join(num)
        num[j] = decrement(original)
        decrement_num = "".join(num)
        if increment_num in mappings:
            adjList[i].append(mappings[increment_num])
        if decrement_num in mappings:
            adjList[i].append(mappings[decrement_num])
        num[j] = original

res = BFS(n,m,adjList,numbers)
if len(res) == 1:
    stdout.write("Neibb\n")
else:
    stdout.write(f"{len(res) - 1}\n")
    stdout.write("\n".join(res))
    stdout.write("\n")
            

