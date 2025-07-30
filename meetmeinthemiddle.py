from math import sqrt

def solve(x1,y1,r1,x2,y2,r2):
    dx = x2 - x1
    dy = y2 - y1
    d = dx ** 2 + dy ** 2
    # no intersection
    if d > (r2 + r1) ** 2:
        return "impossible"
    if d <= (r2 - r1) ** 2:
        # first circle lies inside second circle
        if r2 > r1:
            return "our"
        # second circle lies inside first circle
        else:
            return "their"
    # exactly one point of intersection
    if d == (r2 + r1) ** 2:
        x,y = (r1 * x2 + r2 * x1) / (r1 + r2), (r1 * y2 + r2 * y1) / (r1 + r2)
        return f"compromise\n{x} {y}"

    # two intersection points
    d = sqrt(d)
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = sqrt(r1**2 - a**2)

    # Point along line between centers
    xm = x1 + a * dx / d
    ym = y1 + a * dy / d

    # Offset for intersection points
    rx = -dy * (h / d)
    ry = dx * (h / d)

    # Actual intersection points
    p1 = (xm + rx, ym + ry)
    p2 = (xm - rx, ym - ry)
    p1,p2 = sorted([p1,p2])
    return f"compromises\n{p1[0]} {p1[1]}\n{p2[0]} {p2[1]}"

    
x1,y1,r1 = map(int,input().split())
x2,y2,r2 = map(int,input().split())
print(solve(x1,y1,r1,x2,y2,r2))
