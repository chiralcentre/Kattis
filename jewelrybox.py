from math import sqrt
from sys import stdin,stdout

def largest_volume(x,y):
    h1 = (y + x - sqrt(y**2 - x*y + x**2))/6
    h2 = (y + x + sqrt(y**2 - x*y + x**2))/6
    if h1 < 0:
        return 2*(y - 2*h2)*(x - 2*h2)
    elif h2 < 0:
        return h1 * (y - 2*h1)*(x - 2*h1)
    else:
        return max(h1 * (y - 2*h1)*(x - 2*h1),2*(y - 2*h2)*(x - 2*h2))

for _ in range(int(stdin.readline())):
    x,y = map(int,stdin.readline().split())
    stdout.write(f"{largest_volume(x,y)}\n")
