from sys import stdin

n = int(stdin.readline())
T = [tuple(map(int,stdin.readline().split())) for _ in range(n)]
T.sort(key = lambda x: x[0] + x[1]) # sort by ascending order of completion and mail time
curr = sum(T[0])
for i in range(1,n):
    t,d,c = T[i]
    R = t + d
    if R <= curr: # work has been completed by me and emailed over
        curr += c
    else: # need to wait for the work to be completed and mailed over
        curr = R + c
print(curr)
