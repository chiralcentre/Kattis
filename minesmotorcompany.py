from sys import stdin

N = int(stdin.readline())
stations = [stdin.readline().strip() for _ in range(N)]
total = 0
for i in range(1,N):
    pr,pc = stations[i - 1][0],stations[i - 1][1]
    r,c = stations[i][0],stations[i][1]
    total += abs(ord(pr) - ord(r)) + abs(ord(pc) - ord(c))
print(total)
