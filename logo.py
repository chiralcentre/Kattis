from math import sqrt,sin,cos,radians
from sys import stdin,stdout

class turtle:
    def __init__(self,x=0,y=0,angle=0):
        self.x = x
        self.y = y
        self.angle = angle #measure angle clockwise from North

    def lt(self,a):
        self.angle -= a
        if self.angle < 0:
            self.angle = 360 + self.angle

    def rt(self,a):
        self.angle = (self.angle+a)%360

    def fd(self,d):
        self.x += d*sin(radians(self.angle))
        self.y += d*cos(radians(self.angle))

    def bk(self,d):
        self.x -= d*sin(radians(self.angle))
        self.y -= d*cos(radians(self.angle))

    def distance_from_origin(self):
        return round(sqrt(self.x**2 + self.y**2))
        
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    T = turtle()
    for i in range(n):
        command,num = stdin.readline().split()
        if command == 'fd':
            T.fd(int(num))
        elif command == 'bk':
            T.bk(int(num))
        elif command == 'lt':
            T.lt(int(num))
        else: #rt
            T.rt(int(num))
    stdout.write(f'{T.distance_from_origin()}\n')
