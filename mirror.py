from sys import stdin,stdout

def mirrorLR(image,R,C):
    return [[image[a][C-1-b] for b in range(C)] for a in range(R)]

def mirrorTD(image,R,C):
    return [[image[R-1-a][b] for b in range(C)] for a in range(R)]

for i in range(int(stdin.readline())):
    R,C = map(int,stdin.readline().split())
    image = [list(stdin.readline().strip()) for j in range(R)]
    stdout.write(f'Test {i+1}\n')
    stdout.write('\n'.join(''.join(line) for line in mirrorTD(mirrorLR(image,R,C),R,C))+'\n')
