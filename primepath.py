from sys import stdin,stdout
from collections import deque

def SieveOfEratosthenes(n): #high memory requirements
    primes = [True for i in range(n+1)] #if p[i] == true, i is prime else false
    p,count = 2,n+1
    while p * p <= n:
        if primes[p]: 
            for i in range(p * p, n + 1, p):
                if primes[i]:
                    count -= 1
                primes[i] = False
        p += 1
    primes[0],primes[1] = False,False #0 and 1 are not prime numbers
    return primes,count-2 #exclude 0 and 1

p,c = SieveOfEratosthenes(10000)
primes = {i for i in range(len(p)) if p[i]}

def solve(s,e):
    if s == e:
        return "0"
    visited = [False for _ in range(10000)]
    visited[s] = True
    frontier = deque([(str(s),0)])
    while frontier:
        u,m = frontier.popleft()
        chars = list(u)
        for i in range(4):
            for j in range(10):
                if (i == 0 and j == 0) or j == str(chars[i]):
                    continue
                p = chars[i]
                chars[i] = str(j)
                res = "".join(chars)
                chars[i] = p
                r = int(res)
                if not visited[r] and r in primes:
                    if r == e:
                        return str(m + 1)
                    visited[r] = True
                    frontier.append((res,m + 1))
    return "Impossible"

for _ in range(int(stdin.readline())):
    s,e = map(int,stdin.readline().split())
    stdout.write(f"{solve(s,e)}\n")
