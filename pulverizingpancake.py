from sys import stdin,stdout

N,M = map(int,stdin.readline().split())
columns = list(stdin.readline().strip())
# go from left to right
moves = 0
for i in range(N):
    if columns[i] == "1":
        moves += 1
        if i + 2 < N and columns[i + 1] == "1":
            columns[i + 1] = "0"
            columns[i + 2] = "1"
stdout.write(f"{moves}\n")
