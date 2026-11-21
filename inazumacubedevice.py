from sys import stdin

# let x_i be number of times cube i is struck, p_i be number of petals originally
# note that order of striking is irrelevant
# cube i is solved when x_j + \Sigma_{j: j -> i}{x_j} = -p_i (mod k)
# graph is a DAG alreadu given in topological order, sweep from 0 to n - 1
# Let S_i = \Sigma_{j: j -> i}{x_j} (running sum thus far)
# x_i = d_i - S_i (mod k)
# take r = d_i - S_i (mod k) at each step
# code runs in O(n + m) time
n,m,k = map(int,stdin.readline().split())
P = [-int(stdin.readline()) % k for _ in range(n)]
S = [0 for _ in range(n)]
X = [0 for _ in range(n)]
adjList = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(lambda x: int(x) - 1,stdin.readline().split())
    adjList[a].append(b)
ans = 0
for i in range(n):
    X[i] = (P[i] - S[i]) % k
    ans += X[i]
    for b in adjList[i]:
        S[b] = (S[b] + X[i]) % k
print(ans)
