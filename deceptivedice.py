from math import ceil,floor
n,k = map(int,input().split())
#expected value of 1 roll
E = (n*(n+1)//2)/n
#reroll if first result is <= expected score of k - 1 rolls
for i in range(k-1):
    h = ceil(E)
    if h == E:
        h += 1
    E = ((n-h+1)*(n+h)//2)/n + E*floor(E)/n
print(E)
    
    
