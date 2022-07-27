from sys import stdin,stdout
from collections import deque
from math import ceil
#put incoming requests into a queue
#before requests are added, pop all requests that are at least 1000 ms old
#keep track of maximum size S of the queue
#output ceil(S/k) 
n,k = map(int,stdin.readline().split())
queue,S = deque([]),0
for i in range(n): #O(n)
    arrival = int(stdin.readline())
    while queue and queue[0] + 1000 <= arrival:
        queue.popleft()
    queue.append(arrival)
    if len(queue) > S:
        S = len(queue)
stdout.write(str(ceil(S/k)))
    
    

