from sys import stdin,stdout

bitmask = 0

def solve(u,mask,cost):
    global bitmask,videos
    if mask == bitmask:
        return cost
    if u == len(videos):
        return pow(10,9) # not possible to cover all categories
    newmask = mask | videos[u][1]
    if mask != newmask:
        return min(solve(u + 1, newmask,cost + videos[u][0]), solve(u + 1, mask, cost))
    else:
        return solve(u + 1, mask, cost)
    
N = int(stdin.readline())
videos = []
for i in range(N):
    cost,s = stdin.readline().split()
    mask = 0
    for char in s:
        mask |= (1 << (ord(char) - ord("a")))
    bitmask |= mask
    videos.append((int(cost),mask))
stdout.write(f"{solve(0,0,0)}\n")

