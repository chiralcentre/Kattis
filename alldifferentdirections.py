from math import cos,sin,pi,sqrt

def new_coordinates(pos,d,angle):
    angle = angle*pi/180
    return [pos[0] + d*cos(angle), pos[1] + d*sin(angle)]

def distance(d1,d2):
    return sqrt((d1[0]-d2[0])**2 + (d1[1]-d2[1])**2)
  
while True:
    n = int(input())
    if n == 0:
        break
    counter = 0
    destinations,lengths = [],[]
    while counter < n:
        inpt = input().split()
        start_coord = [float(inpt[0]),float(inpt[1])]
        directions = inpt[2:]
        start,walk = 0,0
        for i in range(0,len(directions),2):
            if directions[i] == 'start':
                start = float(directions[i+1])
            elif directions[i] == 'turn':
                turn = float(directions[i+1])
                start += turn # turn towards left
            elif directions[i] == 'walk':
                walk = float(directions[i+1])
                start_coord = new_coordinates(start_coord,walk,start)
        destinations.append(start_coord)
        counter += 1
    x,y = 0,0
    for place in destinations:
        x += place[0]
        y += place[1]
    average_destination = [x/len(destinations),y/len(destinations)]
    for place in destinations:
        lengths.append(distance(average_destination,place))
    print(f"{average_destination[0]} {average_destination[1]} {max(lengths)}")
                                    


        
      
    
