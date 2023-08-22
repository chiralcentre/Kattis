from sys import stdin,stdout
from math import gcd,pi

for _ in range(int(stdin.readline())):
    seen = set()
    r,n,d,m,s = map(int,stdin.readline().split())
    interval = d * 60 * 60 + m * 60 + s
    # rounds represent the number of rounds going around the circle until the cycle repeats
    rounds = interval // gcd(interval,1296000)
    a = 0
    while rounds > 0 and n > 0:
        seen.add(a)
        a += interval
        if a >= 1296000:
            a %= 1296000
            rounds -= 1
        n -= 1
    ans,area = 0,pi * r * r
    seen = sorted(seen)
    for i in range(1,len(seen)):
        ans = max(ans,(seen[i] - seen[i - 1]) / 1296000 * area)
    ans = max(ans,(1296000 - seen[-1]) / 1296000 * area)
    stdout.write(f"{ans}\n")
