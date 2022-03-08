from math import pi,sqrt,acos
from sys import stdin,stdout
for line in stdin:
    r,x,y = map(float,line.split())
    if x**2 + y**2 > r**2: #miss the cookie
        stdout.write("miss\n")
    else: #shortest chord containing P is perpendicular to OP.
        d = sqrt(x**2 + y**2)
        opposite_length = 2*sqrt(r**2-d**2)
        theta = acos((2*r**2-opposite_length**2)/(2*r**2))
        # subtract area of triangle from sector
        smaller_region = 0.5*r**2*theta - 0.5*d*opposite_length
        larger_region = pi*r**2 - smaller_region
        stdout.write(f'{larger_region} {smaller_region}\n')
        
