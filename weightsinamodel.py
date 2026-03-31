from sys import stdin,stdout

MOD = pow(10,9) + 7
X = list(map(int,stdin.readline().split()))
a,b = map(int,stdin.readline().split())
c,d = map(int,stdin.readline().split())
for i in range(int(stdin.readline())):
    n = int(stdin.readline())
    while len(X) < n:
        p = len(X) + 1
        if p % 2:
            X.append((c * X[-1] + d * X[-2]) % MOD)
        else:
            X.append((a * X[-1] + b * p) % MOD)
    stdout.write(f"{X[n - 1]}\n")
