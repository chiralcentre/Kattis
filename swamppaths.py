from sys import stdin,stdout
from bisect import bisect_left

# assumes a < b
def encode(a,b,M):
    return c * M + d

N,L = map(int,stdin.readline().split())
queries,records = [],{}
for i in range(L):
    w,a,b = stdin.readline().split()
    c,d = sorted([int(a),int(b)])
    H = encode(c,d,N)
    if w != "QUERY":
        if H not in records:
            records[H] = [(i,w)]
        else:
            records[H].append((i,w))
    else:
        queries.append((i,H))
            
# For each path that is queried, if the path status changed (ADD or REMOVE) in an earlier step, we know if the path is safe or not.
# If a queried path has not had its status changed yet, we need to look ahead to see if its status changed some time in the future.
# If so, we know its current state (e.g. if the first change in the future is to ADD it, we know it was not safe during an earlier query).
# The only “unsure” responses are if the status of a queried path never changed at any point in the log.
for i,H in queries:
    if H not in records:
        stdout.write("unsure\n")
    else:
        R = records[H]
        idx = bisect_left(R,i,key = lambda x: x[0]) # only compare off first element
        if idx == 0: # look forward
            stdout.write("safe\n") if R[idx][1] == "REMOVE" else stdout.write("unsafe\n")
        else: # look backward
            idx -= 1
            stdout.write("safe\n") if R[idx][1] == "ADD" else stdout.write("unsafe\n")

    
