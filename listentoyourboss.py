from sys import stdin,stdout,setrecursionlimit
from math import log2

#change recursion limit to 1000000 since up to 100000 recursive calls are needed
setrecursionlimit(10**6)
#Credits to CP4 repository for LCA source code
#Check for LCA using a sparse table in O(log n) time
#overall code runs in O(n log n)
class SparseTable:
  def __init__(self, A=[]):
    self.A = A
    self.P2 = []
    self.L2 = []
    self.SpT = []
    n = len(self.A)
    L2_n = int(log2(n)) + 1
    self.P2 = [0] * (L2_n+1)
    self.L2 = [0] * (2**L2_n+1)
    for i in range(L2_n + 1):
      self.P2[i] = 2**i
      self.L2[2**i] = i
    for i in range(2, self.P2[L2_n]):
      if self.L2[i] == 0:
        self.L2[i] = self.L2[i-1]
    self.SpT = [[None] * n for _ in range(self.L2[n]+1)]
    for j in range(n):
      self.SpT[0][j] = j
    for i in range(1, L2_n+1):
      for j in range(n-self.P2[i]+1):
        x = self.SpT[i-1][j]
        y = self.SpT[i-1][j+self.P2[i-1]]
        self.SpT[i][j] = x if A[x] <= A[y] else y

  def RMQ(self, i, j):
    k = self.L2[j-i+1]
    x = self.SpT[k][i]
    y = self.SpT[k][j-self.P2[k]+1]
    return x if self.A[x] <= self.A[y] else y

def dfs(cur, depth):
  global adjList, L, E, H, idx
  H[cur] = idx
  E[idx] = cur
  L[idx] = depth
  idx += 1
  for nxt in adjList[cur]:
    dfs(nxt, depth + 1)
    E[idx] = cur
    L[idx] = depth
    idx += 1

def buildRMQ():
  global idx, H, N
  idx = 0
  H = [-1] * (N)
  dfs(0, 0)

N,M = map(int,stdin.readline().split())
L,E,H,idx = [0] * (2*N), [0] * (2*N), [0] * (N), 0
adjList = [[] for _ in range(N)]
for i in range(1,N):
    a = int(stdin.readline()) - 1
    adjList[a].append(i)
buildRMQ(); SPT = SparseTable(L)
for i in range(M):
    a,b = map(lambda x: int(x) - 1, stdin.readline().split())
    lower,higher = sorted([H[a],H[b]])
    #arguments for RMQ must be in sorted order
    #E[SPT.RMQ(lower,higher)] gives the LCA of a and b
    #If LCA of a and b is b, order should not be ignored
    stdout.write("No\n") if E[SPT.RMQ(lower,higher)] == b else stdout.write("Yes\n")



