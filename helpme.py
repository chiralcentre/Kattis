from collections import deque
columns = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h'}
rows = {0:8,1:7,2:6,3:5,4:4,5:3,6:2,7:1}
white,black = {'K':[],'Q':[],'R':[],'B':[],'N':[],'P':[]},{'k':[],'q':[],'r':[],'b':[],'n':[],'p':[]}

for i in range(17): #17 rows in total
    line = input().strip()
    if i%2: # odd numbered lines contain the board
        for j in range(2,33,4): #33 characters in a row
            if line[j] in white: #keys of white and black are the pieces
                white[line[j]].append(f'{line[j]}{columns[j//4]}{rows[(i-1)//2]}') if line[j] != 'P' else white[line[j]].append(f'{columns[j//4]}{rows[(i-1)//2]}')
            elif line[j] in black:
                black[line[j]].append(f'{line[j].upper()}{columns[j//4]}{rows[(i-1)//2]}') if line[j] != 'p' else black[line[j]].append(f'{columns[j//4]}{rows[(i-1)//2]}')
# In case two pieces of the same type appear in the input, the piece with the smaller row number must be described before the other one if the pieces are white
# If two pieces of the same type appear in the same row, the one with the smaller column letter must appear first.
for key1 in white:
    white[key1] = sorted(white[key1],key = lambda x:(x[2],x[1])) if key1 != 'P' else sorted(white[key1],key = lambda x:(x[1],x[0])) #pawn board states only have two characters
# The one with the larger row number must be described first if the pieces are black.
for key2 in black:
    black[key2] = sorted(black[key2],key = lambda x:(-int(x[2]),x[1])) if key2 != 'p' else sorted(black[key2],key = lambda x:(-int(x[1]),x[0])) 
    
print("White: ",end='')
print(','.join(','.join(row) for row in white.values() if row))
print("Black: ",end='')
print(','.join(','.join(row) for row in black.values() if row))
