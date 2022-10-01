from math import sqrt

V = int(input())
lowestC = 10**10
#O(V)
for i in range(1,int(sqrt(V)) + 1):
    for j in range(1,int(sqrt(V)) + 1):
        product = i*j
        if not V % product:
            k = V // product
            lowestC = min(lowestC, 2*(i*j + j*k + i*k))
print(lowestC)
