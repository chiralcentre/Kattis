from math import sqrt

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __sub__(self,other):
        if isinstance(other,Point):
            return Point(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __add__(self,other):
        if isinstance(other,Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def dot_prod(self,other):
        if isinstance(other,Point):
            return self.x * other.x + self.y  * other.y
        return NotImplemented

    def scale(self,factor):
        return Point(self.x * factor, self.y * factor)

    def dist(self,other):
        if isinstance(other,Point):
            return sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))
        return NotImplemented

    def __repr__(self):
        return f"Point(x = {self.x}, y = {self.y})"

def side(P, p1, p2):
    d = p2 - p1
    v = P - p1
    return d.x * v.y - d.y * v.x  # cross product sign


A = Point(*map(int,input().split()))
B = Point(*map(int,input().split()))
p1 = Point(*map(int,input().split()))
p2 = Point(*map(int,input().split()))
if side(A,p1,p2) * side(B,p1,p2) < 0: # A and B are on opposing sites of the line, straight line from A to B crosses line
    print(A.dist(B))
else:
    # reflect first point A about line to get A'
    # find distance from A' to second point B, this will be the answer
    # get direction vector of line
    d = p2 - p1
    # vector from p1 to A
    v = A - p1
    # project v onto d to compute foot of perpendicular
    F = p1 + d.scale(v.dot_prod(d) / d.dot_prod(d))
    # foot of perpendicular is midpoint of A and A'
    R = F.scale(2) - A
    print(R.dist(B))

