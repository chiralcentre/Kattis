while True:
    inpt = list(map(float,input().split()))
    if len(inpt) == 1:
        break
    x1,y1,x2,y2,p = inpt
    print(((abs(x1-x2))**p + (abs(y1-y2))**p)**(1/p))
