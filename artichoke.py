from math import sin,cos,radians,inf

def stockprice(p,a,b,c,d,k):
    return p*(sin(a*k+b)+cos(c*k+d)+2)

p,a,b,c,d,n = map(int,input().split())

highest,max_diff = stockprice(p,a,b,c,d,1),0

for i in range(2,n+1):
    current = stockprice(p,a,b,c,d,i)
    if highest < current: #store maximum value thus far 
        highest = current
    elif highest - current > max_diff:
        max_diff = highest - current
        
print(max_diff)
