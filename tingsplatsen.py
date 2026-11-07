from sys import stdin,stdout

N,M = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(N)]
farms = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == "*":
            farms.append((i,j))
# assume there are A farms, A <= N * M
# this code runs in O(NMA) time
for i in range(N):
    for j in range(M):
        if grid[i][j] != "*": # normal cell
            d,possible = None,True
            for x,y in farms:
                t = abs(i - x) + abs(j - y)
                if d == None:
                    d = t
                elif d != t:
                    possible = False
                    break
            stdout.write("X") if possible else stdout.write(".")
        else:
            stdout.write("*")
    stdout.write("\n")
