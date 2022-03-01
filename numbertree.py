line = input().split()
if len(line) > 1:
    H,path = int(line[0]),line[1]
else:
    H,path = int(line[0]),[]
# L and R store the difference between the parent node and the left/right child nodes respectively  
start,L,R = 2**(H+1)-1,1,2
for move in path:
    if move == 'L':
        start -= L
        R += L
        L *= 2    
    if move == 'R':
        start -= R
        L += R
        R *= 2
print(start)
