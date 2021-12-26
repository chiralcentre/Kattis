R,C = list(map(int,input().split()))
grid = [list(input().strip()) for i in range(R)]
squashed = {num: 0 for num in range(5)}

for i in range(R-1):
    for j in range(C-1):
        space = [grid[i][j],grid[i][j+1],grid[i+1][j],grid[i+1][j+1]]
        if '#' not in space:
            squashed[space.count('X')] += 1
            
for key in squashed:
    print(squashed[key])
