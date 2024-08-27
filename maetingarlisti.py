from sys import stdin,stdout

n,r,c = map(int,stdin.readline().split())
rows = [stdin.readline().split() for i in range(r)]
for i in range(r):
    first = stdin.readline().strip()
    for _ in range(c - 2):
        stdin.readline()
    last = stdin.readline().strip()
    stdout.write("left\n") if first == rows[i][0] and last == rows[i][-1] else stdout.write("right\n")
