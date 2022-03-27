from sys import stdin,stdout

quadkey = stdin.readline().strip()
zoom_level,x,y = len(quadkey),0,0
for i in range(zoom_level):
    if quadkey[i] == '1' or quadkey[i] == '3':
        x += 1 << zoom_level >> (i+1) # x += 2**(zoom_level)//(2**(i+1))
    if quadkey[i] == '2' or quadkey[i] == '3':
        y += 1 << zoom_level >> (i+1) # y += 2**(zoom_level)//(2**(i+1))
stdout.write(f'{zoom_level} {x} {y}\n') 
    
