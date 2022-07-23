from sys import stdin,stdout

def solve(intervals):
    low,high = intervals[0]
    for i in range(1,N): #check for overlapping time frames
        L,H = intervals[i]
        if L > low:
            low = L
        if H < high:
            high = H
        if low > high:
            return "edward is right"
    return "gunilla has a point"
    
N = int(stdin.readline())
intervals = [tuple(map(int,stdin.readline().split())) for _ in range(N)]
stdout.write(solve(intervals))
