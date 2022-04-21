from sys import stdin,stdout
from heapq import heappush,heappop,heapify

N,K = map(int,stdin.readline().split())
elements = stdin.readline().split()
elemCount,occurrences = {},[]
for e in elements:
    elemCount[e] = 1 if e not in elemCount else elemCount[e] + 1
for value in elemCount.values():
    occurrences.append(-value) #negation is required since occurrences is a maxheap
heapify(occurrences)
while K > 0: #O(K log N)
    value = heappop(occurrences)
    value += 1
    heappush(occurrences,value)
    K -= 1
stdout.write(f'{-occurrences[0]}') #print maximum occurrence after removal
