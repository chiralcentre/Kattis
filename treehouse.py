from sys import stdin

def findSquares(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    #square 1
    p3a = (p1[0] - dy, p1[1] + dx)
    p4a = (p2[0] - dy, p2[1] + dx)
    #square 2
    p3b = (p1[0] + dy, p1[1] - dx)
    p4b = (p2[0] + dy, p2[1] - dx)
    return (p3a, p4a), (p3b, p4b)

N = int(stdin.readline())
spots = [tuple(map(int,stdin.readline().split())) for _ in range(N)]
available = set(spots)
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        a,b = findSquares(spots[i],spots[j])
        p1,p2,p3,p4 = a[0],a[1],b[0],b[1]
        if p1 in available and p2 in available:
            ans += 1
        if p3 in available and p4 in available:
            ans += 1
# divide by 4 since there are 4 squares counted per square
print(ans >> 2)
        
