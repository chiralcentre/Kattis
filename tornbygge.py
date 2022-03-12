from sys import stdin,stdout

N = int(stdin.readline())
bricks,total = list(map(int,stdin.readline().split())),1
for i in range(1,N):
    if bricks[i] > bricks[i-1]: # new tower is constructed whenever new brick has bigger width than previous brick
        total += 1
stdout.write(f'{total}\n')
        

