from sys import stdin,stdout

def collision(i,j,r,c,grid):
    movements = [(-1,0),(0,1),(1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
    for x,y in movements:
        if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] == '*':
            return True
    return False

def checkSolution(regions,solution):
    stars = [0 for i in range(10)] #keeps track of number of stars in each region
    for i in range(10):
        for j in range(10):
            if solution[i][j] == '*':
                if collision(i,j,10,10,solution): #check for stars in adjacent cells
                    return "invalid"
                else:
                    for k in range(10):
                        if (i,j) in regions[k]:
                            stars[k] += 1
                            break
    #check every region has 2 stars
    for k in range(10):
        if stars[k] != 2:
            return "invalid"
    #check every row has 2 stars
    for i in range(10):
        counter = sum(1 for j in range(10) if solution[i][j] == '*')
        if counter != 2:
            return "invalid"
    #check every column has 2 stars
    for j in range(10):
        counter = sum(1 for i in range(10) if solution[i][j] == '*')
        if counter != 2:
            return "invalid"
    return "valid"

regions = [set() for i in range(10)] #keeps track of coordinates of points in each region
puzzle = [stdin.readline().strip() for _ in range(10)]
for i in range(10):
    for j in range(10):
        regions[int(puzzle[i][j])].add((i,j))
solution = [stdin.readline().strip() for _ in range(10)]
stdout.write(checkSolution(regions,solution))
