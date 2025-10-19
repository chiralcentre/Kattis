from sys import stdin

N,M = map(int,stdin.readline().split())
# sort in ascending order of task completion time, break ties in descending order of grade increase
tasks = sorted([tuple(map(int,stdin.readline().split())) for _ in range(N)], key = lambda x: (x[0],-x[1]))
ans = 0
for T,G in tasks:
    if M >= T:
        M -= T
        ans += G
    else:
        break
print(ans)
