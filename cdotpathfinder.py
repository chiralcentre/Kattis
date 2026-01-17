from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    pairs = list(map(int,stdin.readline().split()))
    time,ans = pow(10,9),-1
    for i in range(n):
        t = pairs[2 * i + 1] / pairs[2 * i]
        if t < time:
            time,ans = t,i + 1
    stdout.write(f"{ans}\n")
