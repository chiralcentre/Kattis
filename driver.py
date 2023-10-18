from sys import stdin,stdout
from math import ceil

N = int(stdin.readline())
tolls,times = list(map(int,stdin.readline().split())),list(map(int,stdin.readline().split()))
lowest = [tolls[0]]
for i in range(1,N - 1):
    if tolls[i] <= lowest[-1]:
        lowest.append(tolls[i])
    else:
        lowest.append(lowest[-1])
        
ans,currTime = 0,0
for i in range(1,len(times)):
    currTime += 1 # 1 hour required to cross the road
    ans += tolls[i - 1]
    if currTime < times[i]: # cannot cross immediately, find smallest road toll so far and go back and forth on that road
        d = times[i] - currTime
        ans += lowest[i - 1] * ceil(d / 2) * 2
        currTime += ceil(d / 2) * 2
stdout.write(f"{ans}\n")
    
