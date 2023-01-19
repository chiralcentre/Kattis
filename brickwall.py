from sys import stdin,stdout,setrecursionlimit

def solve(c1,c2,c3,curr):
    global ans,gaps,H,visited
    visited[c1][c2][c3] = True
    if ans == "YES" or curr > H:
        return
    if curr == H:
        ans = "YES"
        return
    if not gaps[curr + 1] and c1 > 0 and not visited[c1 - 1][c2][c3]:
        solve(c1 - 1,c2,c3,curr + 1)
    if not gaps[curr + 2] and c2 > 0 and not visited[c1][c2 - 1][c3]:
        solve(c1,c2 - 1,c3,curr + 2)
    if not gaps[curr + 3] and c3 > 0 and not visited[c1][c2][c3 - 1]:
        solve(c1,c2,c3 - 1,curr + 3)

#maximum length is 300
gaps,ans = [False for i in range(305)],"NO"
N,c1,c2,c3 = map(int,stdin.readline().split())
row = list(map(int,stdin.readline().split()))
#gaps contain the distances of every connection measured from the left
H = 0
for i in range(N - 1):
    H += row[i]
    gaps[H] = True
H += row[N - 1]
#use visited 3D array to prevent revisiting same state again
visited = [[[False for i in range(c3 + 1)] for j in range(c2 + 1)] for k in range(c1 + 1)]
solve(c1,c2,c3,0)
stdout.write(f"{ans}\n")
