from sys import stdin,stdout

N = int(stdin.readline())
x,y = [],[]
for _ in range(N):
    t,v = map(float,stdin.readline().split())
    x.append(t)
    y.append(v)

counter = sum(((y[i]+y[i+1])/2)*(x[i+1]-x[i]) for i in range(N-1))/1000
stdout.write(f'{counter}\n')
