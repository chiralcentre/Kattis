from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    N,timings = int(stdin.readline()),[]
    for i in range(N):
        w,*pieces = map(int,stdin.readline().split())
        timings.append(sum(p for p in pieces))
    timings.sort() #sort timings in ascending order, and complete the orders in ascending order of timing
    total = sum(timings[i]*(N-i) for i in range(N))
    stdout.write(f"{total/N}\n")
