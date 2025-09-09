from sys import stdin

n = int(stdin.readline())
ans = -1
for i in range(n):
    h,word = stdin.readline().split()
    if word == "nej":
        ans = max(int(h),ans)
print(ans)
