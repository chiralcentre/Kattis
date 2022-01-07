from math import floor,sqrt

def distance(i,j,x,y):
    return sqrt(abs(i-x)**2 + abs(j-y)**2)

x,y,n = map(int,input().split())
points = []
for _ in range(n):
    a,b,c = map(int,input().split())
    points.append((a,b,c))

distances = sorted([distance(a,b,x,y) - c for a,b,c in points])
#maximum three circles         
print(floor(distances[2])) if distances[2] > 0 else print(0)
        
        
    
