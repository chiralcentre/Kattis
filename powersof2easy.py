n,e = map(int,input().split())
substring = str(2**e)
print(sum(1 if substring in str(i) else 0 for i in range(n+1)))
