#by Brahmgupta's theorem, maximum area is achieved when quadrilateral is cyclic
from math import sqrt
a,b,c,d = map(int,input().split())
s = (a+b+c+d)/2
print(sqrt((s-a)*(s-b)*(s-c)*(s-d)))
