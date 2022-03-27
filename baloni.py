from sys import stdin,stdout
from collections import defaultdict

stdin.readline() #N not required
balloons = list(map(int,stdin.readline().split()))
arrows,throws = defaultdict(lambda:0),0 #arrows[h] indicates the number of arrows at height h
for x in balloons:
    if arrows[x+1] > 0:
        arrows[x+1] -= 1 # remove one arrow from the higher height
    else:
        throws += 1 #no arrow at higher height so a new arrow needs to be thrown
    arrows[x] += 1  
stdout.write(f'{throws}\n')
