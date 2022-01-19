from math import pi
# height of the original cone each frustum is part of is D/2.
while True:
    D,V = map(int,input().split())
    if D == 0 and V == 0:
        break
    print(((pi*D**3-6*V)/pi)**(1/3))
