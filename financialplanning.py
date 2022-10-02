from sys import stdin,stdout
from math import ceil

# For each investment, compute the day it starts paying off.
# Sort investments by the day they start paying off.
# Greedily add investments which pay off the soonest as long as
# they do not start paying off after your current retirement day.
n,M = map(int,stdin.readline().split())
investments = []
for _ in range(n):
    p,c = map(int,stdin.readline().split())
    days = ceil(c//p)
    investments.append((p,c,days))
investments.sort(key = lambda x: x[2])
balance,retirement,ans = 0,M,10**10 
for p,c,d in investments:
    retirement += c #cost of retirement
    balance += p #current earnings per days
    ans = min(ans,(retirement + balance - 1)//balance)
stdout.write(f"{ans}")
