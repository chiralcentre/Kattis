import sys

movements = {'left':(0,-1),
             'right':(0,1),
             'up':(-1,0),
             'down':(1,0)}
pos = (0,0)
T,B,L,R = 0,0,0,0
path = [] 
for line in sys.stdin:
    movement = line.strip()
    if not movement: #EOF
        break
    pos = tuple(sum(x) for x in zip(pos,movements[movement]))
    x,y = pos
    if x < T:
        T = x
    elif x > B:
        B = x
    if y < L:
        L = y
    elif y > R:
        R = y
    path.append(pos)

print('#'*(R-L+3)) # there are R-L+3 hashes in each edge of the border
for i in range(T,B+1):
    row = ['#']
    for j in range(L,R+1):
        if i == 0 and j == 0:
            row.append('S')
        elif (i,j) == path[-1]:
            row.append('E')
        elif (i,j) in path:
            row.append('*')
        else:
            row.append(' ')
    row.append('#')
    print(''.join(row))
print('#'*(R-L+3))
