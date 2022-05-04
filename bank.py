from sys import stdin,stdout
from heapq import heappush,heappop

N,T = map(int,stdin.readline().split())
people = [[] for i in range(T)]
for i in range(N): 
    c,t = map(int,stdin.readline().split())
    people[t].append(c)
# start from the highest time slot t as customers can be served at any time before t
highest,money = [],0
for i in range(T-1,-1,-1):
    for c in people[i]:
        heappush(highest,-c) #negate to convert to max heap
    if highest:
        money -= heappop(highest) #choose a candidate for each time slot, starting from t = T - 1 
stdout.write(f'{money}')
    
