from sys import stdin

def solve(words):
    W = "ICPC"
    if len(words) != 4:
        return 0
    for i in range(4):
        if words[i][0] != W[i]:
            return 0
    return 1

words = stdin.readline().split()
print(solve(words))
