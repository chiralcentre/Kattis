from math import log2,floor

N = int(input()) 
print(floor(log2(N))+1)
start = 1
print(start,end = ' ')
while 2*start <= N:
    start *= 2
    print(start, end = ' ')
