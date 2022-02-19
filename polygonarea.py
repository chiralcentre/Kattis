from sys import stdin,stdout

def shoelaceformula(x,y):
    return sum(x[i]*y[i+1] - y[i]*x[i+1] for i in range(len(x)-1))/2

while True:
    n = int(stdin.readline())
    if n == 0:
        break
    x,y = [],[]
    for _ in range(n):
        x1,y1 = map(int,stdin.readline().split())
        x.append(x1); y.append(y1)
    x.append(x[0]); y.append(y[0]) #for shoelace formula calculations
    area = shoelaceformula(x,y)
    stdout.write(f'CCW {area} \n') if area > 0 else stdout.write(f'CW {abs(area)} \n')
    
