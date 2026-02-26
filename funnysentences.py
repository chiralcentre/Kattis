from sys import stdin,stdout

a,b,m = int(stdin.readline()),int(stdin.readline()),int(stdin.readline())
block = [[stdin.readline().strip() for _ in range(m)] for i in range(4)]
n = 1
for _ in range(m):
    ans = []
    for i in range(4):
        n = (a * n + b) % m
        ans.append(block[i][n])
    stdout.write(f"{' '.join(ans)}.\n")
