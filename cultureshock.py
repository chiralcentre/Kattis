from sys import stdin

forbidden = {"he", "she", "him", "her"}
N = int(stdin.readline())
words = stdin.readline().split()
print(sum(1 for i in range(N) if words[i] in forbidden))
