from collections import deque

for _ in range(int(input())):
    # jumps keep track which branch the node splits into
    n,x,y,jumps = 1,1,1,deque([])
    K,f1 = input().split()
    p,q = map(int,f1.split('/'))
    while p != x or q != y: #backtrack
        if q > p: #left node
            q -= p
            jumps.appendleft(0)
        else: #right node
            p -= q
            jumps.appendleft(1)
    for num in jumps:
        n = 2*n if num == 0 else 2*n+1
    print(f'{K} {n}')
