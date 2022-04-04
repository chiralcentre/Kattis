from math import sqrt
x,y,x1,y1,x2,y2 = map(int,input().split())
if x1 <= x <= x2:
    print(min(abs(y-y1),abs(y-y2)))
elif y1 <= y <= y2:
    print(min(abs(x-x1),abs(x-x2)))
else:
    print(sqrt((min(abs(x-x1),abs(x-x2))**2+min(abs(y-y1),abs(y-y2))**2)))
    
