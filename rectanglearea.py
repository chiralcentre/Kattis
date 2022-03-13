from sys import stdin,stdout

x1,y1,x2,y2 = map(float,stdin.readline().split())
stdout.write(f'{abs(x2-x1)*abs(y2-y1)}\n')
