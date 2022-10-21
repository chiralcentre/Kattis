from sys import stdin,stdout

EPSILON = 10**-15
INF = 10**9
def ccw(A,B,C):
    return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])

def intersect(A,B,C,D):
        return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
    
while True:
    n = int(stdin.readline())
    if n == 0:
        break
    lines = [tuple(map(float,stdin.readline().split())) for _ in range(n)]
    triangles = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                x1,y1,x2,y2 = lines[i]
                x3,y3,x4,y4 = lines[j]
                x5,y5,x6,y6 = lines[k]
                #put gradient as 10**9 for vertical lines
                g1 = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else INF 
                g2 = (y4 - y3) / (x4 - x3) if x4 - x3 != 0 else INF
                g3 = (y6 - y5) / (x6 - x5) if x6 - x5 != 0 else INF
                #check that the lines are not parallel
                if not(abs(g1 - g2) < EPSILON or abs(g2 - g3) < EPSILON or abs(g1 - g3) < EPSILON) and (intersect((x1,y1),(x2,y2),(x3,y3),(x4,y4)) and intersect((x1,y1),(x2,y2),(x5,y5),(x6,y6)) and intersect((x3,y3),(x4,y4),(x5,y5),(x6,y6))):
                    triangles += 1
                    
    stdout.write(f"{triangles}\n")
                
