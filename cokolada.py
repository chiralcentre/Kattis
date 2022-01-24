from math import log2,ceil
K = int(input())
D,breaks,counter = 2**ceil(log2(K)),0,0

squares = D
if squares > K:
    while counter < K:
        squares //= 2
        if counter + squares <= K:
            counter += squares    
        breaks += 1

print(f'{D} {breaks}')
    
