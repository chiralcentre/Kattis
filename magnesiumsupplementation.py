from math import sqrt
from sys import stdin,stdout

# O(sqrt(n)) time
n,k,p = map(int,stdin.readline().split())
ans = []
for i in range(1,int(sqrt(n)) + 1):
    r = n // i
    if r * i == n:
        if r <= p and i <= k:
            ans.append(i)
        # prevent duplicates in case of square numbers
        if i != r and i <= p and r <= k:
            ans.append(r)
stdout.write(f"{len(ans)}\n")
stdout.write("\n".join(str(num) for num in sorted(ans)))
            
