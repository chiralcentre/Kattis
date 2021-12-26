n,k = list(map(int,input().split()))
d,s = list(map(int,input().split()))

print((d*n - k*s)/(n-k)) if 0 <= (d*n - k*s)/(n-k) <= 100 else print('impossible')
