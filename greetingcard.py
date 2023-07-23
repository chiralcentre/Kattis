from sys import stdin,stdout

mask = (1 << 31) - 1

# compress the 2D coordinates into a 1D coordinate
def encode(a,b):
    return (a << 31) + b

def decode(c):
    return (c >> 31, c & mask)

#there are only 12 possible points to look at
movements = [(0,2018),(0,-2018),(2018,0),(-2018,0),
             (1118,1680),(-1118,1680),(1118,-1680),(-1118,-1680),
             (1680,1118),(-1680,1118),(1680,-1118),(-1680,-1118)]

points = {}
n = int(stdin.readline())
for i in range(n):
    a,b = map(int,stdin.readline().split())
    c = encode(a,b)
    points[c] = 1 if c not in points else points[c] + 1

ans = 0
for p,v in points.items():
    a,b = decode(p)
    for x,y in movements:
        if a + x >= 0 and b + y >= 0:
            h = encode(a + x, b + y)
            if h in points:
                ans += v * points[h]
stdout.write(f"{ans >> 1}\n") #divide by 2 to account for dupes

             
