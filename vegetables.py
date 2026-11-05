from sys import stdin
from heapq import heappop,heappush,heapify

class Node:
    def __init__(self,num,denom):
        self.num = num
        self.denom = denom

    def __lt__(self, other):
        return self.num * other.denom < other.num * self.denom
    
T,N = stdin.readline().strip().split()
T,N = int(T[2:]),int(N)
# negate to convert from min heap to max heap
# runs in O(N + A log N) where A is number of cuts, bounded by 500 here
heap,L,cuts = [],pow(10,18),0
for w in map(int,stdin.readline().split()):
    heap.append(Node(-w,1))
    L = min(w,L)
d = 1
heapify(heap)
while True:
    node = heappop(heap)
    w,k = -node.num,node.denom
    if 100 * L * k > T * w * d:
        break
    heappush(heap,Node(-w,k + 1))
    cuts += 1
    if w * d < L * (k + 1):
        L,d = w,k + 1
print(cuts)
    
