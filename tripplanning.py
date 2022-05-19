from sys import stdin,stdout

N,M = map(int,stdin.readline().split())
#connected[a] = b means that train line b connects city a to city (a+1)%N
#connected[a] = -1 means that there is no train line connecting city a to city (a+1)%N
connected = [-1 for i in range(N)]; trains = 0
for i in range(M):
    a,b = map(int,stdin.readline().split())
    a -= 1; b -= 1 #offset by 1 due to zero indexing
    x = min(a,b); y = max(a,b);
    if y == x + 1:
        connected[x] = i + 1
        trains += 1
    if x == 0 and y == N - 1:
        connected[y] = i + 1
        trains += 1
stdout.write("impossible") if trains != N else stdout.write("\n".join(str(line) for line in connected))
    
