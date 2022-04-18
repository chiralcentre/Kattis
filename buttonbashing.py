from sys import stdin,stdout
from collections import deque

def optimalBFS(n,t,buttons):
    if t == 0:
        return 0
    # there are 3600s in an hour
    visited,frontier = [False for _ in range(3601)],deque([(0,0)]) #right attribute keeps track of number of jumps
    visited[0] = True
    while frontier:
        u,counter = frontier.popleft()
        for move in buttons:
            v = u+move
            if v < 0:
                v = 0
            elif v > 3600:
                v = 3600
            if v == t:
                return counter+1
            if not visited[v]:
                visited[v] = True
                frontier.append((v,counter+1))
    return -1 #exact time cannot be found

def suboptimalBFS(n,t,buttons):
    if t == 0:
        return 0,0
    # there are 3600s in an hour
    visited,frontier = [False for _ in range(3601)],deque([(0,0)]) #right attribute keeps track of number of jumps
    visited[0] = True
    minimalPresses,lowestTime = 0,3601
    while frontier:
        u,counter = frontier.popleft()
        for move in buttons:
            v = u+move
            if v < 0:
                v = 0
            elif v > 3600:
                v = 3600
            if v >= t and lowestTime > v:
                minimalPresses,lowestTime = counter+1,v
            if not visited[v]:
                visited[v] = True
                frontier.append((v,counter+1))
    return minimalPresses,lowestTime-t

for _ in range(int(stdin.readline())):
    n,t = map(int,stdin.readline().split())
    buttons = list(map(int,stdin.readline().split()))
    x = optimalBFS(n,t,buttons)
    if x > -1:
        stdout.write(f'{x} 0\n')
    else:
        a,b = suboptimalBFS(n,t,buttons)
        stdout.write(f'{a} {b}\n')
    
