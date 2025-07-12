from sys import stdin

# code runs in O(N log N) time
N,K = map(int,stdin.readline().split())
acorns = list(map(int,stdin.readline().split()))
# sizes[i] reprsents the acorn sizes for remainder of i
sizes = [[],[],[],[]]
for a in acorns:
    sizes[a % 4].append(a)
for i in range(len(sizes)):
    sizes[i] = sorted(sizes[i])
curr = K
while sizes[curr % 4]:
    curr += sizes[curr % 4].pop()
print(curr)
