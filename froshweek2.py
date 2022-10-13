from sys import stdin,stdout

n,m = map(int,stdin.readline().split())
#O(n log n)
tasks = sorted(map(int,stdin.readline().split()))
#O(m log m)
quiet = sorted(map(int,stdin.readline().split()))
idx1,idx2 = n-1, m-1
while idx1 > -1 and idx2 > -1:
    if quiet[idx2] >= tasks[idx1]:
        idx2 -= 1
    idx1 -= 1
stdout.write(f"{m - 1 - idx2}")  
        
