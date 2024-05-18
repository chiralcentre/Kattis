from sys import stdin

# count minimum number of walls between elements i to i + M - 1
# ensure that there are walls at elements i - 1 and elements i + M
# use prefix sums
# O(N) time complexity
N,M = map(int,stdin.readline().split())
s = stdin.readline().strip()
prefix_walls = [0 for _ in range(N)]
if s[0] == "#":
    prefix_walls[0] += 1
for i in range(1,N):
    if s[i] == "#":
        prefix_walls[i] += 1
    prefix_walls[i] += prefix_walls[i - 1]

best = pow(10,9)
for i in range(1,N - M):
    if s[i - 1] == "#" and s[i + M] == "#":
        best = min(best, prefix_walls[i + M - 1] - prefix_walls[i - 1])
print("Neibb") if best == pow(10,9) else print(best)
