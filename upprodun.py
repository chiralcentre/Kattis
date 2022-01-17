from math import ceil
N,M = int(input()),int(input())
average = ceil(M/N)

while M%N:
    M -= average
    N -= 1
    print('*'*average)
    
for _ in range(N):
    print('*'*(M//N))
 
    
