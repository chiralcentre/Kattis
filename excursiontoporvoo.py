from sys import stdin,stdout

n,m = map(int,stdin.readline().split())
edges = []
for _ in range(m):
    i,d,c = map(int,stdin.readline().split())
    edges.append((i,d,c))
# sort in decreasing order of capacity in O(m log m)
edges.sort(key = lambda x: -x[2])
q = int(stdin.readline())
# sort queries for car in decreasing order of weight in O(q loq q) time
# this means that the active set of connections only increases as weight of car decreases
queries = sorted([(int(stdin.readline()),i) for i in range(q)], key = lambda x: -x[0])
# best[i] contains contains cost of cheapest usable road from i to i + 1
# S = sum of all finite best[i]
# missing = number of gaps still at None
# this code runs in O(m + q) time
best = [None for _ in range(n)]
answers = [None for _ in range(q)]
S,missing,edge_ptr = 0,n - 1,0
for w,i in queries:
    while edge_ptr < m and edges[edge_ptr][2] >= w:
        idx,d,c = edges[edge_ptr]
        if best[idx] is None:
            best[idx] = d
            S += d
            missing -= 1
        elif best[idx] > d:
            S -= best[idx] - d
            best[idx] = d
        edge_ptr += 1
    answers[i] = str(S) if missing == 0 else "impossible"
stdout.write("\n".join(answers))
stdout.write("\n")
