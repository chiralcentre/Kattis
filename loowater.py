from sys import stdin,stdout

while True:
    n,m = map(int,stdin.readline().split())
    if n == m == 0:
        break
    dragons = sorted([int(stdin.readline()) for _ in range(n)], reverse = True)
    knights = sorted([int(stdin.readline()) for _ in range(m)], reverse = True)
    gold = 0
    while knights and dragons:
        h = knights.pop()
        if dragons[-1] <= h:
            gold += h
            dragons.pop()
    stdout.write("Loowater is doomed!\n") if dragons else stdout.write(f"{gold}\n")
