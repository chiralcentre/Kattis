a,b = map(int,input().split())
if b - a >= 0:
    print(b - a)
else:
    ops = 0
    while a > b:
        if a%2:
            a += 1
        else:
            a //= 2
        ops += 1
    ops += (b - a)
    print(ops)
        
