from sys import stdin,stdout
from heapq import heappush,heappop,heapify

# think backwards: what is the minimum ink required to merge blocks of distinct colors into one?
for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    canvasses = list(map(int,stdin.readline().split()))
    #convert to min heap in O(N) time
    heapify(canvasses)
    #While we have more than one item
    #Pop the two smallest items A and B
    #Add A + B to the result
    #Push A + B into the priority queue
    sol = 0
    while len(canvasses) > 1: #O(N log N)
        A,B = heappop(canvasses),heappop(canvasses)
        sol += A + B
        heappush(canvasses,A+B)
    stdout.write(f"{sol}\n")

