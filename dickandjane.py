from sys import stdin,stdout

for line in stdin:
    s,p,y,j = map(int,line.split())
    # Let Yertle's age be c, Puff's age be b and Spot's age be a.
    c = (12 + j - y - p)//3
    b = c + p; a = c + y
    if 12 + j - (a + b + c) == 2: #if difference is 2
        a += 1; b += 1
    elif 12 + j - (a + b + c) == 1: # if difference is 1
        if s < a - b:
            b += 1
        else:
            a += 1
    stdout.write(f'{a} {b} {c}\n')
    
    
