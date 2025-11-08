from sys import stdin

print(len({stdin.readline().strip() for _ in range(int(stdin.readline()))}) + 1)
