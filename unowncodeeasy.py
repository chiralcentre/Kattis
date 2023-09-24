from sys import stdin,stdout
from math import floor,log10,gcd

def numOfDigits(n):
    return floor(log10(n) + 1)

def lcm(a,b):
    return a * b // gcd(a,b)

#find period
def period(n):
    M = pow(10,numOfDigits(n))
    s = n
    # By Pigeonhole Principle, period cannot exceed M
    for i in range(M):
        s *= n
        s %= M
        if s == n:
            return i + 1
    return -1

def solve(N,groups):
    periods = []
    # O(N * max(a_i))
    for i in range(N):
        p = period(groups[i])
        if p == -1:
            return -1
        periods.append(p)
    # find LCM of all periods in O(N * log(a_i))
    for i in range(1,N):
        periods[i] = lcm(periods[i],periods[i - 1])
    return periods[N - 1] + 1
    
N = int(stdin.readline())
groups = list(map(int,stdin.readline().split()))
stdout.write(f"{solve(N,groups)}\n")
