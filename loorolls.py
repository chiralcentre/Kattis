l,n = map(int,input().split())
k = 1
while l%n:
    n -= l%n
    k += 1
print(k)
