from sys import stdin,stdout

S,N = map(int,stdin.readline().split())
occupied,additional = list(map(int,stdin.readline().split())),0
for i in range(N-1): 
    additional += (occupied[i+1] - occupied[i] - 2)//2
#wrap around
additional += (occupied[0] + S - occupied[N-1] - 2)//2
stdout.write(f'{additional}\n')
