from sys import stdin

X = list(map(float,stdin.readline().split()))
if len(X) < 3:
    print("At least 3 scores needed!")
else:
    print(f"Sum of scores (3 lowest removed): {sum(sorted(X)[3:])}")
