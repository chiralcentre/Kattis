from sys import stdin,stdout

def possible(N,T,potions):
    for i in range(N):
        potions[i] -= (N-i-1)*T
        if potions[i] <= 0:
            return "NO"
    return "YES"

N,T = map(int,stdin.readline().split())
potions = sorted([int(stdin.readline()) for _ in range(N)],reverse=True) #O(N log N)
stdout.write(possible(N,T,potions))
