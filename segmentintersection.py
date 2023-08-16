from sys import stdin,stdout

def inRange(a,b,c):
    return min(b,c) <= a <= max(b,c)

# checks if interval [a,b] intersects interval [c,d]
def intersect(a,b,c,d):
    a,b = sorted([a,b])
    c,d = sorted([c,d])
    return a <= d and c <= b

# checks if the two segments (x1,y1) to (x2,y2) and (x3,y3) to (x4,y4) intersect
def segments_intersect(x1,y1,x2,y2,x3,y3,x4,y4):
    dx1,dy1 = x2 - x1,y2 - y1
    dx2,dy2 = x4 - x3,y4 - y3
    # check if either line segment is degenerate
    firstLineIsPoint,secondLineIsPoint = (dx1 == 0 and dy1 == 0), (dx2 == 0 and dy2 == 0)
    # third condition is to check if point lies on line
    if firstLineIsPoint and not secondLineIsPoint:
        return f"{'%.2f' % x1} {'%.2f' % y1}" if inRange(x1,x3,x4) and inRange(y1,y3,y4) and (x4 - x3) * y2 + (y4 - y3) * x3 == (y4 - y3) * x2 + y3 * (x4 - x3) else "none"
    elif not firstLineIsPoint and secondLineIsPoint:
        return f"{'%.2f' % x3} {'%.2f' % y3}" if inRange(x3,x1,x2) and inRange(y3,y1,y2) and (x2 - x1) * y4 + (y2 - y1) * x1 == (y2 - y1) * x4 + y1 * (x2 - x1) else "none"
    elif firstLineIsPoint and secondLineIsPoint:
        return f"{'%.2f' % x1} {'%.2f' % y1}" if (x1,y1) == (x4,y4) else "none"
    else: # both are line segments
        # note that if the two segments are parallel, dy1/dx1 = dy2/dx2
        # dx2 * dy1 = dy2 * dx1
        if dx2 * dy1 == dy2 * dx1:
            # segments are parallel, check if they intersect
            # check if y intercepts in equations of both lines are the same
            if dx2 * (dx1 * y1 - dy1 * x1) == dx1 * (dx2 * y3 - dy2 * x3):
                points = sorted([(x1,y1),(x2,y2),(x3,y3),(x4,y4)])
                a,b,c,d = points[1][0],points[1][1],points[2][0],points[2][1]
                if intersect(x1,x2,x3,x4) and intersect(y1,y2,y3,y4):
                    return f"{'%.2f' % a} {'%.2f' % b} {'%.2f' % c} {'%.2f' % d}" if a != c or b != d else f"{'%.2f' % a} {'%.2f' % b}"
            return "none" # lines are parallel and non intersecting
        else:
            xa,ya = -1,-1
            # check if either line segment is vertical
            if dx1 == 0 or dx2 == 0:
                xa = x1 if dx1 == 0 else x3
                if dx1 == 0:
                    g2 = dy2 / dx2
                    c2 = y3 - g2 * x3
                    ya = g2 * xa + c2
                else:
                    g1 = dy1 / dx1
                    c1 = y1 - g1 * x1
                    ya = g1 * xa + c1
            else: 
                g1,g2 = dy1 / dx1, dy2 / dx2
                c1,c2 = y1 - g1 * x1, y3 - g2 * x3
                xa = (c2 - c1) / (g1 - g2)
                ya = g1 * xa + c1
            return f"{'%.2f' % xa} {'%.2f' % ya}".replace("-0.00","0.00") if inRange(xa,x1,x2) and inRange(xa,x3,x4) and inRange(ya,y1,y2) and inRange(ya,y3,y4) else "none"

for _ in range(int(stdin.readline())):
    x1,y1,x2,y2,x3,y3,x4,y4 = map(int,stdin.readline().split())
    stdout.write(f"{segments_intersect(x1,y1,x2,y2,x3,y3,x4,y4)}\n")
