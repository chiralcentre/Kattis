L,D,N = map(int,input().split())
birds = sorted([int(input()) for _ in range(N)])
if N > 0:
    extra = (birds[0]-6)//D + (L-6-birds[-1])//D
    for i in range(N-1):
        if (birds[i+1] - birds[i]) >= 2*D:
            extra += (birds[i+1] - birds[i])//D - 1
else:
    extra = (L-12)//D + 1
print(extra)
