from sys import stdin,stdout
from collections import deque

def SieveOfEratosthenes(n): #O(n log(log n))
    primes = [True for i in range(n+1)] #if p[i] == true, i is prime else false
    p = 2
    while (p * p <= n):
        if (primes[p]): 
            for i in range(p**2, n + 1, p):
                primes[i] = False
        p += 1
    primes[0],primes[1] = False,False #0 and 1 are not prime numbers
    return primes

def possiblepositions(i,j,r,c):
    movements = [(-1,0),(1,0),(0,-1),(0,1)] #up, down, left, right
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] == 0]

def BFS(x,y):
    if x == y:
        return "0"
    a1,b1 = coordinates[x]
    a2,b2 = coordinates[y]
    visited = [[False for i in range(100)] for j in range(100)]
    visited[a1][b1] = True
    frontier = deque([(a1,b1,0)]) #third coordinate keeps track of number of jumps
    while frontier:
        i,j,steps = frontier.popleft()
        for m,n in possiblepositions(i,j,100,100):
            if m == a2 and n == b2:
                return str(steps + 1)
            if not visited[m][n]:
                frontier.append((m,n,steps+1))
                visited[m][n] = True
    return "impossible" #no possible path

#maximum grid size is 10000
grid = [[-1 for i in range(100)] for j in range(100)]
primeSieve = SieveOfEratosthenes(10000)
directions = ["right","down","left","up"]
#use DAT to store coordinates of every point
coordinates = [0 for _ in range(10001)]

#populate grid starting from top left
counter,currentX,currentY,currentDir = 10000,0,0,0
while counter > 1:
    nxtX,nxtY = currentX,currentY
    if directions[currentDir] == "right":
        nxtY += 1
    elif directions[currentDir] == "down":
        nxtX += 1
    elif directions[currentDir] == "left":
        nxtY -= 1
    else:
        nxtX -= 1
    #check for out of bounds or visited
    if nxtX < 0 or nxtX >= 100 or nxtY < 0 or nxtY >= 100 or grid[nxtX][nxtY] > -1:
        currentDir = (currentDir + 1)%4
    else:
        grid[currentX][currentY] = counter if primeSieve[counter] else 0
        coordinates[counter] = (currentX,currentY) #update coordinates
        currentX,currentY = nxtX,nxtY
        counter -= 1
#manually configure for number 1 
grid[50][49] = 0;coordinates[1] = (50,49)
num = 1
for line in stdin:
    x,y = map(int,line.split())
    stdout.write(f"Case {num}: {BFS(x,y)}\n")
    num += 1
