from sys import stdin,stdout

# O(2 ^ n) backtracking
def solve(u,mask,sc_size):
    global bitmask,n,adjMat
    if mask == bitmask: # all vertices are covered
        return sc_size
    if u == n:
        return pow(10,9) # not possible to cover all vertices
    # choose to place an ad or not
    return min(solve(u + 1, mask, sc_size), solve(u + 1, mask | adjMat[u], sc_size + 1))
    
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    adjMat = [0 for _ in range(n)]
    bitmask = (1 << n) - 1
    for i in range(n):
        d,*conn = map(int,stdin.readline().split())
        for j in range(d):
            a = conn[j] - 1 #offset by 1 due to zero indexing
            adjMat[i] |= 1 << a
            adjMat[a] |= 1 << i
        adjMat[i] |= 1 << i # self loop, every vertex is connected to itself
    stdout.write(f"{solve(0,0,0)}\n")
