def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def left_shift(m):
    for row in m:
        for _ in range(len(m[0])-1): #move across empty tiles
            for k in range(len(m[0])-1):
                if row[k] == 0 and row[k+1] > 0:
                    row[k],row[k+1] = row[k+1],row[k]
    return m

def left_merge(m):
    m = left_shift(m)
    for row in m:
        for k in range(len(m[0])-1):
            if row[k] > 0 and row[k] == row[k+1]:
                row[k] *= 2
                row[k+1] = 0
    return left_shift(m)

def right_shift(m):
    for row in m:
        for _ in range(len(m[0])-1): #move across empty tiles
            for k in range(len(m[0])-1,0,-1):
                if row[k] == 0 and row[k-1] > 0:
                    row[k],row[k-1] = row[k-1],row[k]
    return m

def right_merge(m):
    m = right_shift(m)
    for row in m:
        for k in range(len(m[0])-1,0,-1):
            if row[k-1] > 0 and row[k-1] == row[k]:
                row[k] *= 2
                row[k-1] = 0
    return right_shift(m)

def up_merge(m):
    m = transpose(m)
    m = left_merge(m)
    return transpose(m)

def down_merge(m):
    m = transpose(m)
    m = right_merge(m)
    return transpose(m)
    
# The resulting tile cannot merge with another tile again in the same move.   
grid = [list(map(int,input().split())) for _ in range(4)]
moves = {0: left_merge, 1: up_merge, 2: right_merge, 3: down_merge}
print('\n'.join(' '.join(list(map(str,row))) for row in moves[int(input())](grid)))
            
