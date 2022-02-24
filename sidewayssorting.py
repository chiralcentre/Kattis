from sys import stdin,stdout
from functools import cmp_to_key

def compare(x,y):
    # arrange in ascending order
    return 1 if x.lower() > y.lower() else 0 if x.lower() == y.lower() else -1

first = True
while True:
    r,c = map(int,stdin.readline().split())
    if r == 0 and c == 0:
        break
    if first:
        first = False
    else:
        stdout.write('\n')
    rows = [list(stdin.readline().strip()) for _ in range(r)]
    columns = [''.join([rows[i][j] for i in range(r)]) for j in range(c)]
    columns.sort(key = cmp_to_key(compare)) #python sorted function is stable
    for m in range(r):
        for k in range(c):
            stdout.write(columns[k][m])
        stdout.write('\n') 
    
