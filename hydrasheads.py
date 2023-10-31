from sys import stdin,stdout
from collections import deque

def solve(H,T):
    # make dimensions sufficiently large
    visited = [[-1 for i in range(1000)] for j in range(1000)]
    visited[H][T] = 0; frontier = deque([(H,T,0)])
    while frontier:
        h,t,w = frontier.popleft()
        # if number of tails are odd, cut off one tail to grow back two new tails
        if visited[h][t + 1] == -1: 
            visited[h][t + 1] = w + 1
            frontier.append((h,t + 1,w + 1))
        # cut off two heads
        if h >= 2 and visited[h - 2][t] == -1:
            if h == 2 and t == 0:
                return w + 1
            visited[h - 2][t] = w + 1
            frontier.append((h - 2,t,w + 1))
        # cut off two tails
        if t >= 2 and visited[h + 1][t - 2] == -1:
            visited[h + 1][t - 2] = w + 1
            frontier.append((h + 1,t - 2,w + 1))
    return -1

for line in stdin:
    H,T = map(int,line.split())
    if H == T == 0:
        break
    stdout.write(f"{solve(H,T)}\n")
    
