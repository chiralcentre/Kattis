from math import sqrt,ceil

def distance(pos1,pos2):
    return sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)

for i in range(int(input())):
    points = 0
    for j in range(int(input())):
        coordinates = tuple(map(int,input().split()))
        d = distance((0,0),coordinates)
        if d == 0:
            points += 10
        elif 0 < d <= 200: #points cannot be negative
            points += 11 - ceil(d/20)
    print(points)   
