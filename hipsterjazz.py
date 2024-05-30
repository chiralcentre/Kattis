from sys import stdin,stdout

N,M = map(int,stdin.readline().split())
adjList = [[] for _ in range(N)]
side,otherSide = [False for _ in range(N)],[0 for _ in range(N)]
for i in range(M):
    a,b = map(lambda x: int(x) - 1, stdin.readline().split())
    adjList[a].append(b)
    adjList[b].append(a)

loop = True
# restart process of assigning instruments if condition of having at least half of friends play other instrument is not met
# at the start, everyone has same instrument
while loop:
    loop = False
    for i in range(N):
        sameSide = len(adjList[i]) - otherSide[i]
        # more than half of friends play the same instrument, swap instrument
        if sameSide > otherSide[i]:
            for v in adjList[i]:
                if side[i] != side[v]:
                    otherSide[i] -= 1
                    otherSide[v] -= 1
            side[i] = not side[i] # invert instrument
            for v in adjList[i]:
                if side[i] != side[v]: 
                    otherSide[i] += 1
                    otherSide[v] += 1
            loop = True
            break
stdout.write("".join("PS"[int(side[i])] for i in range(N)))
