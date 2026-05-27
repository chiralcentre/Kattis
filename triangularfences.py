import math

def cross2d(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def point_in_triangle(p, t):
    """Point p inside triangle t (clockwise winding)"""
    for i in range(3):
        if cross2d(t[i], t[(i+1)%3], p) > 0:
            return False
    return True

def dist_point_segment(p, a, b):
    dx, dy = b[0]-a[0], b[1]-a[1]
    if dx == 0 and dy == 0:
        return math.hypot(p[0]-a[0], p[1]-a[1])
    t = max(0.0, min(1.0, ((p[0]-a[0])*dx + (p[1]-a[1])*dy) / (dx*dx + dy*dy)))
    return math.hypot(p[0]-a[0]-t*dx, p[1]-a[1]-t*dy)

def min_dist(t1, t2):
    d = float('inf')
    for i in range(3):
        for j in range(3):
            a, b = t1[i], t1[(i+1)%3]
            c, e = t2[j], t2[(j+1)%3]
            d = min(d, dist_point_segment(a,c,e), dist_point_segment(b,c,e),
                       dist_point_segment(c,a,b), dist_point_segment(e,a,b))
    return d

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
t1 = [(nums1[i*2], nums1[i*2+1]) for i in range(3)]
t2 = [(nums2[i*2], nums2[i*2+1]) for i in range(3)]
contained = (all(point_in_triangle(p, t2) for p in t1) or
             all(point_in_triangle(p, t1) for p in t2))
print("YES" if contained else "NO")
print(f"{min_dist(t1, t2)}")
