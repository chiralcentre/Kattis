N,M = list(map(int,input().split()))
sizes = list(map(int,input().split()))

seats,rejected = 0,M
for i in range(M):
    if seats + sizes[i] <= N:
        seats += sizes[i]
        rejected -= 1
    else:
        break
        
print(rejected)
