from sys import stdin,stdout

#returns (a,b,c)
def getLineCoeff(x1,y1,x2,y2):
    r1,r2 = y2 - y1,x2 - x1
    return (-r1,r2,r1*x1 -r2*y1)

#squared distance from a point(x0,y0) to a line ax + by + c = 0 is (ax0 + by0 + c)^2/(a^2 + b^2)
#Note: comparing numerator should be sufficient since denominator is the same, I am not sure why it did not work
def pointToLine(a,b,c,x0,y0):
    return (a*x0 + b*y0 + c)**2 / (a**2 + b**2)

for _ in range(int(stdin.readline())):
    x1,y1,x2,y2 = map(int,stdin.readline().split())
    #determine a,b,c
    a,b,c = getLineCoeff(x1,y1,x2,y2)
    m = int(stdin.readline())
    low,ans = 10**9,[]
    for _ in range(m):
        p,*coords = stdin.readline().split()
        x0,y0 = map(int,coords)
        d = pointToLine(a,b,c,x0,y0)
        if d == low:
            ans.append(p)
        elif d < low:
            low = d
            ans = [p]
    stdout.write(" ".join(city for city in ans))
    stdout.write("\n")
