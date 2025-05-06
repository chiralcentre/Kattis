from sys import stdin,stdout
from functools import cmp_to_key

def compare(p1,p2):
    a,b = p1
    c,d = p2
    LHS,RHS = a * d, b * c
    return LHS - RHS if LHS != RHS else c - a

n = int(stdin.readline())
resources = [tuple(map(int,stdin.readline().split())) for _ in range(n)]
# sort in ascending order of g / r and descending order of numerator when first condition is tied
resources.sort(key = cmp_to_key(compare))
for x,y in resources:
    stdout.write(f"{x} {y}\n")
