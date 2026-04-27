from sys import stdin
from heapq import heapify,heappush,heappop

class Person:
    def __init__(self,t,i):
        self.t = t
        self.index = i

    def __lt__(self,other):
        return self.t < other.t
    
n,k = map(int,stdin.readline().split())
T = list(map(int,stdin.readline().split()))
queue = [Person(T[i],i + 1) for i in range(k)]
heapify(queue)
for i in range(n):
    res = heappop(queue)
    print(res.index, flush = True)
    read = stdin.readline().strip()
    if read == "DONE":
        continue
    heappush(queue,Person(int(read),res.index))
print("DONE")
