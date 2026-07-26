from sys import stdin
from math import ceil

n = int(stdin.readline())
word_count,woke = 0,0
for _ in range(n):
    line = stdin.readline().strip("\n").split()
    word_count += len(line)
    for w in line:
        if w.count("-") >= 2:
            woke += 1
print(f"Þessi texti er {ceil(woke / word_count * 100)}% woke.")
