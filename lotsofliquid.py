from sys import stdin

n = int(stdin.readline())
sides = list(map(float,stdin.readline().split()))
total_volume = sum(L ** 3 for L in sides)
print(pow(total_volume, 1 / 3))
