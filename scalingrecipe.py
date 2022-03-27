from sys import stdin,stdout

n,x,y = map(int,stdin.readline().split())
for i in range(n):
    stdout.write(f'{int(int(stdin.readline())*y/x)}\n')
