def landpositions(grid,r,c): #possible positions for coffeeshop
    # a set is used to reduce time taken to check if a coordinate is in landpositions
    return {(i,j) for i in range(r) for j in range(c) if grid[i][j] == '.'}

def adjacentpositions(i,j,r,c):
    movements = [(-1,0),(0,1),(1,0),(0,-1)]
    return [(i+x,j+y) for x,y in movements if i+x in range(r) and j+y in range(c)]

def coffee_shop_placement(grid,r,c):
    land_pn = landpositions(grid,r,c)
    while land_pn:
        x,y = land_pn.pop()
        grid[x][y] = 'E'
        for position in adjacentpositions(x,y,r,c):
            if position in land_pn:
                land_pn.remove(position) #coffee shops cannot be adjacent to each other
                
        
n,m = map(int,input().split())
grid = [list(input().strip()) for _ in range(n)]
coffee_shop_placement(grid,n,m)
print('\n'.join(''.join([char for char in row]) for row in grid))
