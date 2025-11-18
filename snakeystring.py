from sys import stdin

r,c = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(r)]
string = [grid[j][i] for i in range(c) for j in range(r) if grid[j][i] != "."]
print("".join(string))
        
