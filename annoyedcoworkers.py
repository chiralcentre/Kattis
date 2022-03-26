from sys import stdin,stdout
from heapq import heappush,heappop,heapify

h,c = map(int,stdin.readline().split())
#left attribute stores annoyance level upon request for help, right attribute stores increase
coworkers,highest = [],-1
for _ in range(c):
    x,y = map(int,stdin.readline().split())
    if x > highest: highest = x #record highest amount if not all coworkers are used
    coworkers.append((x+y,y))
heapify(coworkers) #O(c)

for i in range(h): #O(h log c)
    a,d = heappop(coworkers)
    if a > highest:
        highest = a
    heappush(coworkers,(a+d,d))
stdout.write(f'{highest}\n')
