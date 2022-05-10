from sys import stdin,stdout
from heapq import heappush,heappop

N = int(stdin.readline())
deliveryList = []; highestTime = -1
for i in range(N):
    t,c = map(int,stdin.readline().split())
    deliveryList.append((t,c))
    if t > highestTime:
        highestTime = t
timeslots = [[] for _ in range(highestTime)]
for t,c in deliveryList:
    timeslots[t-1].append(c) #offset by 1 due to zero indexing
#start from the highest timeslot as customers can be served at any time before that
PQ,money = [],0
for i in range(highestTime - 1,-1,-1):
    for c in timeslots[i]:
        heappush(PQ,-c) #negate to convert to max heap
    if PQ:
        money -= heappop(PQ) #choose the most optimal candidate from each time slot each available
stdout.write(f'{money}')
