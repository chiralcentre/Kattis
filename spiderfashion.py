L,n,m = map(int,input().split())

if n == 1 or m == 1:
    print(-1)
elif n == 2 or m == 2:
    if L % 2:
        print(-1)
    else:
        shoes,socks = [],[]
        for i in range(0,L,2):
            shoes.append("1")
            shoes.append("2")
            socks.append("2")
            socks.append("1")
        print(2)
        print(" ".join(shoes))
        print(" ".join(socks))
else: # always possible when n > 2 and m > 2
    print(3)
    shoes,socks = [],[]
    for i in range(0,L - 1,2):
        shoes.append("1")
        shoes.append("2")
        socks.append("2")
        socks.append("3")
    if L % 2:
        shoes.append("3")
        socks.append("1")
    print(" ".join(shoes))
    print(" ".join(socks))
    
