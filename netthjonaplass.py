from sys import stdin,stdout

N = int(stdin.readline())
widths = sorted([int(stdin.readline()) for _ in range(N)])
halves = [widths[0]]
for i in range(1,N):
    d = widths[i] - widths[i - 1]
    halves.append(d - halves[-1])
for h in halves:
    stdout.write(f"{h << 1}\n")
