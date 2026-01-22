from sys import stdin,stdout

M = int(stdin.readline())
plates = list(map(int,stdin.readline().split()))
N,E = map(int,stdin.readline().split())
events,T = [[] for _ in range(10001)],-1
for _ in range(E):
    t,p = map(int,stdin.readline().split())
    events[t].append(p)
    T = t
# let chef be at index 0
queue,curr,p_curr = [0 for _ in range(N + 1)],0,0
costs = [0 for _ in range(N + 1)]
for i in range(T + 1):
    if queue[curr] == 0:
        queue[curr] = plates[p_curr]
        p_curr = (p_curr + 1) % M
    for p in events[i]:
        P = (curr + p) % (N + 1)
        costs[p] += queue[P]
        queue[P] = 0
    curr = (curr - 1) % (N + 1)
for i in range(1, N + 1):
    stdout.write(f"{costs[i]}\n")
