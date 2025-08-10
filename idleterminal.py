from sys import stdin
from heapq import heappush,heappop,heapify

# Simulate the processing of the migration jobs and find the largest gap.
# For each of the n jobs, find the first available CPU core, and update this core’s end time.
# code runs in O(n log k) time
n,k = map(int,stdin.readline().split())
jobs = list(map(int,stdin.readline().split()))
cores,prev,ans = [],0,-1
for i in range(n):
    if len(cores) < k:
        heappush(cores,jobs[i])
    else:
        L = heappop(cores)
        ans = max(L - prev, ans)
        prev = L
        heappush(cores, jobs[i] + L)
while cores:
    L = heappop(cores)
    ans = max(L - prev, ans)
    prev = L
print(ans)
