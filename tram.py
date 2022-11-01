from sys import stdin,stdout

#square of distance from every point(xi,yi) to line = (a + xi - yi)^2/2
#taking first derivative and setting to zero,
#value of a that minimises total unusefulness = -sum(xi - yi for all i)/n
N = int(stdin.readline())
counter = 0
for i in range(N):
    x,y = map(int,stdin.readline().split())
    counter += x - y
stdout.write(f"{-counter/N}")
