from sys import stdin,stdout
from collections import deque
n,p,k = map(int,stdin.readline().split())
p /= 100
timestamps = deque(map(int,stdin.readline().split()))
if timestamps[0] != 0:
    timestamps.appendleft(0)
if timestamps[-1] != k:
    timestamps.append(k)
stdout.write(f"{sum((timestamps[i] - timestamps[i-1])*(1 + (i-1)*p) for i in range(1,len(timestamps)))}")

    
        
