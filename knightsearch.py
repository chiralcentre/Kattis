from sys import stdin,stdout
from collections import deque

letter = {"I": "C", "IC": "P", "ICP": "C", "ICPC": "A",
          "ICPCA": "S", "ICPCAS": "I", "ICPCASI": "A",
          "ICPCASIA": "S", "ICPCASIAS": "G"}

def possiblepositions(i,j,r,c):
    movements = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

def solve(N,S):
    pos = {}
    frontier = deque([(i//N,i%N,"I") for i in range(N**2) if S[i] == "I"])
    while frontier:
        x,y,s = frontier.popleft()
        for a,b in possiblepositions(x,y,N,N):
            ns = s + letter[s]
            if S[a*N + b] == letter[s]:
                frontier.append((a,b,ns))
                if len(ns) == 10:
                    return "YES"
    return "NO"
        
    
N = int(stdin.readline())
S = stdin.readline()
stdout.write(solve(N,S))

