from itertools import permutations
from sys import stdin,stdout

R = int(stdin.readline())
routines = [set(stdin.readline().strip()) for _ in range(R)]
adjMat = [[0 for i in range(R)] for j in range(R)]
# precompute edge weights
for i in range(R):
    for j in range(i + 1,R):
        adjMat[i][j] = adjMat[j][i] = len(routines[i].intersection(routines[j]))
        
minimum,lst = 10**9,[i for i in range(R)]
for perm in permutations(lst):
    counter = sum(adjMat[perm[i]][perm[i + 1]] for i in range(R - 1))
    minimum = min(counter,minimum)
stdout.write(f"{minimum}\n")

