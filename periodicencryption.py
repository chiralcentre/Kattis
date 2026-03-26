from sys import stdin

n,k = map(int,input().split())
s = list(input().strip())
ans = []
curr = 0
while s:
    curr += k - 1
    curr %= len(s)
    ans.append(s[curr])
    s.pop(curr)
print("".join(ans))
