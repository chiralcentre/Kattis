from sys import stdin,stdout
from heapq import heappush,heappop
'''
class Moose:
    def __init__ (self,year,strength):
        self.year = year
        self.strength = strength

    def __lt__(self,otherMoose):
        return self.strength < otherMoose.strength
'''    
def isKarlAlgtavTheWinner(contestants,y,p,n): #O(n log k)
    PQ = []
    for j in range(n):
        for c in contestants[j]: #negate to convert to max heap
            heappush(PQ,(-c,False)) if c != p or j + OFFSET != y else heappush(PQ,(-c,True))
        a,isKarlAlgtav = heappop(PQ)
        if isKarlAlgtav:
            return str(j + OFFSET)
    return "unknown"

k,n = map(int,stdin.readline().split())
#exactly k of the moose will have 2011 as their year of entry,
#and that the remaining n-1 moose will have unique years of entry.
#strength of each moose is unique
OFFSET = 2011
contestants = [[] for _ in range(n)] #there are n unique years
y,p = map(int,stdin.readline().split())
contestants[y-OFFSET].append(p)
for i in range(n+k-2):
    year,strength = map(int,stdin.readline().split())
    contestants[year-OFFSET].append(strength)
stdout.write(isKarlAlgtavTheWinner(contestants,y,p,n))
