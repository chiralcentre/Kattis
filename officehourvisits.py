from sys import stdin,stdout

# sort TAs in ascending order based on end time
# greedily select TAs with shorter end time
N = int(stdin.readline())
events = sorted([tuple(map(int, stdin.readline().split())) for _ in range(N)], key = lambda x: x[1])
end,ans = -1,0
for s,e in events:
    if s >= end:
        ans += 1
        end = e
print(ans)
