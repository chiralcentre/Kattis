from sys import stdin,stdout
from heapq import heappop, heappush
# Python's implementation of PQ is done using a min heap
n,m = map(int,stdin.readline().split())
arrivals,departures,saves = [],[],0
for _ in range(n):
    a,s = map(int,stdin.readline().split())
    heappush(arrivals,a)
    heappush(departures,a+s)

while arrivals:
    time = heappop(arrivals)
    #departures[0] represents smallest element in min heap
    while time - departures[0] > m: #no saves made since the computer will have to be manually unlocked anyways
        heappop(departures)
    # if a resarcher arrives just after another one has left, a save is made
    if departures[0] <= time:
        heappop(departures)
        saves += 1
        
stdout.write(f'{saves}\n')
    
    
