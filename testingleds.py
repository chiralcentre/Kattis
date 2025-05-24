from sys import stdin

ans = pow(10,15)
for i in range(int(stdin.readline())):
    M,O = map(int,stdin.readline().split())
    if O == 0 and M < ans:
        ans = M
print(ans) if ans != pow(10,15) else print(-1)
