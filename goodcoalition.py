from sys import stdin,stdout

# variant of knapsack, runs in O(150N) for each test case
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    W,V = [],[]
    for i in range(n):
        s,p = map(int,stdin.readline().split())
        W.append(s)
        V.append(p / 100)
    memo = [[0 for i in range(151)] for j in range(n + 1)]
    best = -1
    for i in range(n + 1):
        for j in range(151):
            if j == 0:
                memo[i][j] = 1
            elif W[i - 1] <= j:
                b,c = -1,-1
                if memo[i - 1][j] != 0:
                    b = memo[i - 1][j]
                if memo[i - 1][j - W[i - 1]] != 0:
                    c = memo[i - 1][j - W[i - 1]]
                memo[i][j] = max(b,c * V[i - 1])
                memo[i][j] = max(memo[i][j],0)
                if j >= 76 and memo[i][j] > best:
                    best = memo[i][j]
            else:
                memo[i][j] = memo[i - 1][j]
    stdout.write(f"{best * 100}\n")
    
