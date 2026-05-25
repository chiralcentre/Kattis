from collections import defaultdict
from sys import stdin,stdout

def solve():
    n = int(input())
    student_cliques = defaultdict(list)
    
    for i in range(n):
        _,*parts = stdin.readline().split()
        for s in parts:
            student_cliques[s].append(i)
    
    # bridge[i][j] = a student in both clique i and clique j
    bridge = [[None]*n for _ in range(n)]
    for s, cl in student_cliques.items():
        for a in range(len(cl)):
            for b in range(a+1, len(cl)):
                i, j = cl[a], cl[b]
                if bridge[i][j] is None:
                    bridge[i][j] = bridge[j][i] = s
    
    # Floyd-Warshall on clique graph
    INF = float('inf')
    dist = [[INF]*n for _ in range(n)]
    nxt  = [[-1]*n  for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0; nxt[i][i] = i
    for i in range(n):
        for j in range(n):
            if i != j and bridge[i][j]:
                dist[i][j] = 1; nxt[i][j] = j
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k]
    
    def clique_path(ci, cj):
        path = [ci]
        while ci != cj:
            ci = nxt[ci][cj]
            path.append(ci)
        return path
    
    q = int(stdin.readline())
    for _ in range(q):
        u, v = stdin.readline().split()
        if u == v:
            stdout.write(f"0 {u}\n")
            continue
        if u not in student_cliques or v not in student_cliques:
            stdout.write("-1\n")
            continue
        
        best, best_ci, best_cj = INF, -1, -1
        for ci in student_cliques[u]:
            for cj in student_cliques[v]:
                if dist[ci][cj] < best:
                    best, best_ci, best_cj = dist[ci][cj], ci, cj
        
        if best == INF:
            stdout.write("-1\n")
            continue
        cp = clique_path(best_ci, best_cj)
        path = [u]
        for k in range(len(cp)-1):
            path.append(bridge[cp[k]][cp[k+1]])
        path.append(v)
        stdout.write(f"{len(path)} {' '.join(path)}\n")

solve()
