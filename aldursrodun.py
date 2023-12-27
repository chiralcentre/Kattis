from itertools import permutations
from math import gcd

# time complexity of O(n! * n)
def adjacent_gcd(perm):
    for i in range(1,len(perm)):
        if gcd(perm[i],perm[i - 1]) == 1:
            return False
    return True

def solve(n,children):
    for perm in permutations(children):
        if adjacent_gcd(perm):
            return " ".join(str(num) for num in perm)
    return "Neibb"

n,children = int(input()),list(map(int,input().split()))
print(solve(n,children))
