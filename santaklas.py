from math import sin,radians,floor
H,v = map(int,input().split())
if 0 <= v <= 180: # moving horizontally if v == 0 or v == 180, and moving upwards if 0 < v < 180
    print('safe')
else: #Santa Klas is flying at 1 metre per second
    acute_angle = v - 180 if 180 < v <= 270 else 360 - v
    print(floor(H/(sin(radians(acute_angle))))) #take floor
