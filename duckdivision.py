from math import sqrt

D,U = map(int,input().split())
ans = D
for i in range(2,int(sqrt(D))+1):
    if not D%i:
        r = D // i
        if i >= U:
            ans = U
            break
        elif r >= U:
            ans = min(ans,r)
print(ans)
