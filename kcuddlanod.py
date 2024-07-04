special = {"5": "2", "2": "5"}

def invert(s):
    return int("".join(special.get(s[i], s[i]) for i in range(len(s) - 1, -1, -1)))

N,M = input().strip().split()
print([1,2][invert(N) < invert(M)])
