def transpose(m): return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def reverse(m): return [list(reversed(row)) for row in m]

def lShift(m):
    for row in m:
        for _ in range(len(m[0])-1): #move across empty tiles
            for k in range(len(m[0])-1):
                if row[k] == 0 and row[k+1] > 0: row[k],row[k+1] = row[k+1],row[k]      
    return m

def lMerge(m):
    m = lShift(m)
    for row in m:
        for k in range(len(m[0])-1):
            if row[k] > 0 and row[k] == row[k+1]: row[k],row[k+1] = row[k]*2,0
    return lShift(m)

def rMerge(m): m = reverse(m); m = lMerge(m); return reverse(m)

def uMerge(m): m = transpose(m); m = lMerge(m); return transpose(m)

def dMerge(m): m = transpose(m); m = rMerge(m); return transpose(m)

grid,moves = [list(map(int,input().split())) for _ in range(4)],{0: lMerge,1: uMerge,2: rMerge,3: dMerge}
print('\n'.join(' '.join(list(map(str,row))) for row in moves[int(input())](grid)))
            
