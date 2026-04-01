from sys import stdin

ans = 0
for _ in range(int(stdin.readline())):
    u,d = map(int,stdin.readline().split())
    if u % 8 and not (1 <= d <= 10000):
        ans += 1
print(ans)
