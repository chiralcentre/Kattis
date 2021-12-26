a,b,h = list(map(int,input().split()))

d,n = 0,0

while True:
    d += a
    n += 1
    if d >= h:
        break
    d -= b
    
print(n)
