from sys import stdin

n,d = map(int,stdin.readline().split())
m = list(map(int,stdin.readline().split()))
curr,ans = 0,0
while m[curr] != 0:
    ans += m[curr]
    m[curr] = 0
    curr = (curr + d) % n
print(ans)
