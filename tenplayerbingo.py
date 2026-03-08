from sys import stdin

nums = list(map(int,stdin.readline().split()))
d = nums[-1] % 10
if d == 0:
    d = 10
print(d)
