from itertools import permutations
from sys import stdin,stdout

def check_combi(combi):
    global adjMat
    for i in range(len(combi) - 1):
        if adjMat[combi[i]][combi[i + 1]] == 1:
            return False
    return True
    
while True:
    try: n = int(stdin.readline())
    except: break
    names = sorted([stdin.readline().strip() for i in range(n)])
    hashmap,reverse = {i: names[i] for i in range(n)},{names[i]: i for i in range(n)}
    m = int(stdin.readline())
    adjMat = [[-1 for _ in range(n)] for i in range(n)]
    for i in range(m):
        a,b = stdin.readline().split()
        c,d = reverse[a],reverse[b]
        adjMat[c][d] = 1; adjMat[d][c] = 1
    indices = [j for j in range(n)]
    found = False
    for perm in permutations(indices):
        if check_combi(perm):
            stdout.write(" ".join(hashmap[index] for index in perm))
            stdout.write("\n")
            found = True
            break
    if not found:
        stdout.write("You all need therapy.\n")

        
        
