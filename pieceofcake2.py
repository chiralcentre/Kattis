n,h,v = map(int,input().split())
print(max(h*v*4,(n-h)*v*4,h*(n-v)*4,(n-h)*(n-v)*4))
