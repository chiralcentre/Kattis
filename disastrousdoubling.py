from sys import stdin,stdout

def bacteria_left(n,experiments):
    balance = 1
    for i in range(n):
        balance *= 2
        used = experiments[i]
        if used > balance:
            return "error"
        balance -= used
    return str(balance%(10**9+7))

n = int(stdin.readline())
experiments = list(map(int,stdin.readline().split()))
stdout.write(bacteria_left(n,experiments))
