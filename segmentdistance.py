from sys import stdin,stdout
from math import hypot

# calculates distance between the two segments (x1,y1) to (x2,y2) and (x3,y3) to (x4,y4)
def segments_distance(x1,y1,x2,y2,x3,y3,x4,y4):
    if segments_intersect(x1,y1,x2,y2,x3,y3,x4,y4): return 0
    # take minimum of distance from each of the 4 vertices to other segment
    return min(point_segment_distance(x1,y1,x3,y3,x4,y4),
               point_segment_distance(x2,y2,x3,y3,x4,y4),
               point_segment_distance(x3,y3,x1,y1,x2,y2),
               point_segment_distance(x4,y4,x1,y1,x2,y2))

# checks if the two segments (x1,y1) to (x2,y2) and (x3,y3) to (x4,y4) intersect
# this function treats the segments as parameterised vectors
# X = x1 + t * (x2 - x1), X = x3 + s * (x4 - x3)
# Y = y1 + t * (y2 - y1), Y = y3 + s * (y4 - y3)
# if the segments intersect, both s and t are between 0.0 and 1.0
def segments_intersect(x1,y1,x2,y2,x3,y3,x4,y4):
    dx1,dy1 = x2 - x1,y2 - y1
    dx2,dy2 = x4 - x3,y4 - y3
    delta = dx2 * dy1 - dy2 * dx1
    if delta == 0: return False  # parallel segments
    s = (dx1 * (y3 - y1) + dy1 * (x1 - x3)) / delta
    t = (dx2 * (y1 - y3) + dy2 * (x3 - x1)) / (-delta)
    return 0 <= s <= 1 and 0 <= t <= 1

# calculate distance from point (px,py) to line segment (x1,y1) to (x2,y2)
# this function treats segment as parameterised vector where t varies from 0 to 1
def point_segment_distance(px,py,x1,y1,x2,y2):
    dx,dy = x2 - x1,y2 - y1
    if dx == dy == 0:  # the segment's just a point
        return hypot(px - x1, py - y1)
    
    # Calculate the t that minimizes the distance.
    t = ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)

    # See if this represents one of the segment's end points or a point in the middle.
    if t < 0:
        dx,dy = px - x1,py - y1
    elif t > 1:
        dx,dy = px - x2,py - y2
    else:
        dx = px - (x1 + t * dx)
        dy = py - (y1 + t * dy)
    return hypot(dx, dy)

for _ in range(int(stdin.readline())):
    x1,y1,x2,y2,x3,y3,x4,y4 = map(int,stdin.readline().split())
    stdout.write(f"{'%.2f' % segments_distance(x1,y1,x2,y2,x3,y3,x4,y4)}\n")
