import sys

def distance_squared(x1,y1,x2,y2):
    return (x1 - x2)**2 + (y1 - y2)**2

def escape():
    for line in sys.stdin:
        coordinates = line.split()
        if len(coordinates) == 4:
            g1,g2,d1,d2 = map(float,coordinates)
        elif len(coordinates) == 2:
            h1,h2 = map(float,coordinates)
            if 4*distance_squared(g1,g2,h1,h2) <= distance_squared(d1,d2,h1,h2): #dog is two times faster than gopher
                return f'The gopher can escape through the hole at ({format(h1,".3f")},{format(h2,".3f")}).'
    return 'The gopher cannot escape.'

print(escape())
