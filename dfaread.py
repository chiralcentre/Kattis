from sys import stdin,stdout

n,c,s,f = map(int,stdin.readline().split())
w = stdin.readline().strip()
mapping = {w[i]: i + 1 for i in range(len(w))}
final = set(map(int,stdin.readline().split()))
adjMat = [list(map(int,stdin.readline().split())) for _ in range(n)]
for _ in range(int(stdin.readline())):
    line = stdin.readline().strip()
    curr = s
    for char in line:
        curr = adjMat[curr - 1][mapping[char] - 1]
    stdout.write("accept\n") if curr in final else stdout.write("reject\n")
