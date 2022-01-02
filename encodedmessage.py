from math import sqrt

def rotate90Anticlockwise(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

for i in range(int(input())):
    encrypted = list(input().strip())
    length = int(sqrt(len(encrypted)))
    square = rotate90Anticlockwise([encrypted[j*length:j*length+length] for j in range(length)])
    string = [char for row in square for char in row]
    print(''.join(string))
   
