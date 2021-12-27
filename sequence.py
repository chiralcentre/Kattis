from math import log2,floor

N = int(input()) 
print(floor(log2(N))+1)
start = 1
while start <= N:
    print(start, end = ' ')
    start *= 2
    
