from math import sqrt
# square peg can only fit into circular hole if diagonal <= diameter of circular hole
L,R = map(int,input().split())
print("fits") if sqrt(2*L**2) <= 2*R else print("nope")

