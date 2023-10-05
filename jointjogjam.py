from math import hypot

# find maximum of distance between starting points or between ending points
# proof: by differentiation of distance formula
x1,y1,x2,y2,x3,y3,x4,y4 = map(int,input().split())
print(max(hypot(x1 - x2,y1 - y2),hypot(x3 - x4,y3 - y4)))
