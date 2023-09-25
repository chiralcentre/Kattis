from sys import stdin,stdout
from math import floor,log10,gcd

def numOfDigits(n):
    return floor(log10(n) + 1)

def verify(n,t,M):
    return pow(n,t + 1,M) == n

def lcm(a,b):
    return a * b // gcd(a,b)

#observation: period is always of the form 2 ^ x * 5 ^ y for some x >= 0 and y >= 0
def solve(N,groups):
    M = pow(10,numOfDigits(max(groups)))
    x,y = int(log10(M)/log10(2)) + 1, int(log10(M)/log10(5)) + 1
    # log^2(a) periods
    periods = []
    for i in range(x):
        for j in range(y):
            temp = pow(2,i) * pow(5,j)
            if temp > M:
                break
            periods.append((temp,i,j))
    periods.sort()
    # find period for a_1
    j,base = 0,pow(10,numOfDigits(groups[0]))
    while not verify(groups[0],periods[j][0],base):
        j += 1
        if j >= len(periods):
            return -1
    # a, b are the powers for 2 and 5 in the period of a_1
    ans,a,b = periods[j]
    for i in range(1,N):
        base = pow(10,numOfDigits(groups[i]))
        t,c,d = periods[j]
        while not verify(groups[i],t,base) or (c < a or d < b):
            j += 1
            if j >= len(periods):
                return -1
            t,c,d = periods[j]
        ans,a,b = lcm(ans,t),c,d
    return 1 + ans

N = int(stdin.readline())
groups = list(map(int,stdin.readline().split()))
stdout.write(f"{solve(N,groups)}\n")

