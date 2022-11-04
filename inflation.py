from sys import stdin,stdout

def solve(n,canisters):
    highest_fraction = 1000000000
    for i in range(n):
        if canisters[i] > i + 1:
            return "impossible"
        highest_fraction = min(highest_fraction, canisters[i] / (i + 1))
    return str(highest_fraction)

n = int(stdin.readline())
canisters = sorted(map(int,stdin.readline().split()))
stdout.write(solve(n,canisters))
