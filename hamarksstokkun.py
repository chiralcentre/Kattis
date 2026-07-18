from sys import stdin

stdin.readline()
cards = stdin.readline().strip().split()
print(" ".join(cards[::-1]))
