from sys import stdin,stdout

#question is equivalent to finding maximum number of non overlapping intervals
G,N = map(int,stdin.readline().split())
events = [tuple(map(int,stdin.readline().split())) for _ in range(N)]
#sort by departure timing in O(N log N)
events.sort(key = lambda x: x[1])
r = events[0][1]; counter = 1
for i in range(1,N):
    L,R = events[i]
    if L >= r:
        r = R
        counter += 1
stdout.write("YES") if counter >= G else stdout.write("NO")
