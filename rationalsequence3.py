from collections import deque

for _ in range(int(input())):
    # jumps keep track which branch the node splits into
    n,x,y,jumps = 1,1,1,deque([])
    K,N = map(int,input().split())
    while N > n:
        jumps.appendleft('R') if N%2 else jumps.appendleft('L')
        N //= 2
    for branch in jumps:
        if branch == 'L':
            y += x
        else:
            x += y
    print(f'{K} {x}/{y}')
