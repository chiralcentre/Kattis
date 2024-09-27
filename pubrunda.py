from sys import stdin,stdout

ans,best = None,-1
for _ in range(int(stdin.readline())):
    p,k,t = stdin.readline().split()
    time_taken = int(t) * (int(k) + 1)
    if time_taken > best:
        ans,best = p,time_taken
stdout.write(f"{ans} {best}\n")
