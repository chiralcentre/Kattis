from math import ceil,floor
r,f = map(int,input().split())
rota = ceil(f/r) if ceil(f/r) - f/r < f/r - floor(f/r) else floor(f/r)
print("up") if not rota % 2 else print("down")
