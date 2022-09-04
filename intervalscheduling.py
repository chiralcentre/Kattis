from sys import stdin,stdout

n = int(stdin.readline())
#sort by end time in O(n log n)
intervals = sorted([tuple(map(int,stdin.readline().split())) for _ in range(n)],key = lambda x: x[1])
r = intervals[0][1]; counter = 1
for i in range(1,n):
    s,f = intervals[i]
    if s >= r:
        r = f
        counter += 1
stdout.write(f"{counter}")
