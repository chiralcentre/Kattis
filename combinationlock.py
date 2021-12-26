import sys
# 9 degrees difference per graduation
def combinationlock(s,a,b,c):
    # turn dial clockwise 2 full turns
    degrees = 720
    # stop at first number of combination
    degrees += 360 - (a-s)*9 if a > s else (s-a)*9
    #print(degrees)
    # turn the dial counter-clockwise 1 full turn
    degrees += 360
    # continue turning counter-clockwise until the 2nd number is reached
    degrees += (b-a)*9 if b > a else 360 - (a-b)*9
    #print(degrees)
    #turn the dial clockwise again until the 3rd number is reached
    degrees += 360 - (c-b)*9 if c > b else (b-c)*9
    #print(degrees)
    return degrees

for line in sys.stdin:
    start,a,b,c = list(map(int,line.split()))
    if (start,a,b,c) == (0,0,0,0):
        break
    print(combinationlock(start,a,b,c))
    
